"""The Automower integration."""
import asyncio
import copy
import logging
from datetime import datetime

import voluptuous as vol
from homeassistant.components.vacuum import (
    SUPPORT_BATTERY,
    SUPPORT_PAUSE,
    SUPPORT_RETURN_HOME,
    SUPPORT_STATUS,
    SUPPORT_STOP,
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,
    VacuumEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    ATTR_BATTERY_CHARGING,
    ATTR_BATTERY_LEVEL,
    ATTR_STATE,
    CONF_ICON,
    CONF_PASSWORD,
    CONF_USERNAME,
)
from homeassistant.core import HomeAssistant
from homeassistant.util import slugify
from pyhusmow import API as HUSMOW_API

from .const import (
    DEFAULT_ICON,
    DOMAIN,
    ERROR_MESSAGES,
    IGNORED_API_STATE_ATTRIBUTES,
    MODELS,
    STATUS_EXECUTING_PARK,
    STATUS_EXECUTING_START,
    STATUS_EXECUTING_STOP,
    STATUS_OK_CHARGING,
    STATUS_OK_CUTTING,
    STATUS_OK_CUTTING_MANUAL,
    STATUS_OK_LEAVING,
    STATUS_OK_SEARCHING,
    STATUSES,
    SUPPORTED_FEATURES,
    VENDOR,
)

CONFIG_SCHEMA = vol.Schema({DOMAIN: vol.Schema({})}, extra=vol.ALLOW_EXTRA)
_LOGGER = logging.getLogger(__name__)

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS = ["vacuum"]


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Automower component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Automower from a config entry."""
    # TODO Store an API object for your platforms to access
    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {"entities": []}

    hass.data[DOMAIN][entry.entry_id] = HUSMOW_API()
    api = HUSMOW_API()
    #    username = entry.data.get(CONF_USERNAME)
    #    password = entry.data.get(CONF_PASSWORD)
    #    await hass.async_add_executor_job(api.login(username, password))
    api.login(entry.data.get(CONF_USERNAME), entry.data.get(CONF_PASSWORD))

    robots = api.list_robots()
    #    robots = await hass.async_add_executor_job(hass.data[DOMAIN][entry.entry_id].list_robots())
    if not robots:
        return False

    for robot in robots:
        _LOGGER.debug("Robot: %s", robot)
        hass.data[DOMAIN]["entities"].append(AutomowerEntity(robot, api))
    #    return True

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in PLATFORMS
            ]
        )
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class AutomowerEntity(VacuumEntity):
    """Representation of an Automower device."""

    def __init__(self, meta, api):
        """Initialisation of the Automower device."""
        _LOGGER.debug("Initializing device: %s", meta["name"])
        self._id = meta["id"]
        self._name = meta["name"]
        self._model = meta["model"]
        self._state = meta["status"]
        self._mower_status = self._state["mowerStatus"]
        self._stored_timestamp = None
        self._see = None

        # clone already authenticated api client and
        # select automower for this instance
        self._api = copy.copy(api)
        self._api.select_robot(self._id)

    @property
    def id(self):
        """Return the id of the Automower."""
        return self._id

    @property
    def unique_id(self):
        """Return the unique id of the Automower."""
        return self._id

    @property
    def dev_id(self):
        """Return the device id of the Automower (for device tracker)."""
        return slugify("{0}_{1}_{2}".format(DOMAIN, self._model, self._id))

    @property
    def name(self):
        """Return the name of the Automower."""
        return self._name

    @property
    def model(self):
        """Return the model of the Automower."""
        return MODELS.get(self._model, self._model)

    @property
    def icon(self):
        """Return the icon for the frontend based on the status."""
        return STATUSES.get(self._mower_status, {}).get("icon", DEFAULT_ICON)

    # @property
    # def status(self):
    #     """Return the status of the automower as a nice formatted text (for vacuum platform)."""
    #     return self._mower_status.lower()

    @property
    def state(self):
        """Return the state of the automower (same as status)."""
        return self._mower_status.lower()

    @property
    def device_class(self):
        """Return the device class of the automower state."""
        return f"{DOMAIN}__state"

    @property
    def device_info(self):
        """Device info for automower robot."""
        info = {"identifiers": {(DOMAIN, self._id)}, "name": self._name}
        if True:
            info["manufacturer"] = VENDOR
            info["model"] = MODELS.get(self._model, self._model)
        return info

    @property
    def device_state_attributes(self):
        """Return the state attributes of the automower."""
        if self._state is None:
            return {}

        attributes = dict(self._state)

        # Parse timestamps
        for key in ["lastErrorCodeTimestamp", "nextStartTimestamp", "storedTimestamp"]:
            if key in attributes:
                if isinstance(attributes[key], int):
                    # Sometimes(tm), Husqvarna will return a timestamp in millis :(
                    if attributes[key] > 999999999999:
                        attributes[key] /= 1000.0
                    attributes[key] = datetime.fromtimestamp(attributes[key]).strftime(
                        "%Y-%m-%d %H:%M"
                    )

        # Ignore some unneeded attributes & format error messages
        ignored_attributes = list(IGNORED_API_STATE_ATTRIBUTES)
        if attributes["lastErrorCode"] > 0:
            attributes["lastErrorMessage"] = ERROR_MESSAGES.get(
                attributes["lastErrorCode"]
            )
        else:
            ignored_attributes.extend(
                ["lastErrorCode", "lastErrorCodeTimestamp", "lastErrorMessage"]
            )
        if attributes["nextStartSource"] == "NO_SOURCE":
            ignored_attributes.append("nextStartTimestamp")
        attributes[ATTR_BATTERY_LEVEL] = self._state.get("batteryPercent", 100)
        attributes["status"] = self.state
        return sorted(
            {k: v for k, v in attributes.items() if k not in ignored_attributes}.items()
        )

    # @property
    # def battery(self):
    #     """Return the battery level of the automower (for device_tracker)."""
    #     if self._state == None:
    #         return 100
    #     return self._state.get('batteryPercent', 100)

    # @property
    # def battery_level(self):
    #     """Return the battery level of the automower (for vacuum)."""
    #     return self.battery

    @property
    def supported_features(self):
        """Flag supported features."""
        return SUPPORTED_FEATURES

    @property
    def lat(self):
        """Return the current latitude of the automower."""
        return self._state["lastLocations"][0]["latitude"]

    @property
    def lon(self):
        """Return the current longitude of the automower."""
        return self._state["lastLocations"][0]["longitude"]

    @property
    def should_poll(self):
        """Automower devices need to be polled."""
        return True

    @property
    def is_on(self):
        """Return true if automower is starting, charging, cutting, or returning home."""
        return self._mower_status in [
            STATUS_EXECUTING_START,
            STATUS_OK_CHARGING,
            STATUS_OK_CUTTING,
            STATUS_OK_LEAVING,
            STATUS_OK_SEARCHING,
            STATUS_OK_CUTTING_MANUAL,
        ]

    def turn_on(self, **kwargs):
        """Start the automower unless on."""
        if not self.is_on:
            _LOGGER.debug("Sending START command to: %s", self._name)
            self._api.control("START")
            self._mower_status = STATUS_EXECUTING_START
            self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        """Stop the automower unless off."""
        if self.is_on:
            _LOGGER.debug("Sending STOP command to: %s", self._name)
            self._api.control("STOP")
            self._mower_status = STATUS_EXECUTING_STOP
            self.schedule_update_ha_state()

    def start_pause(self, **kwargs):
        """Toggle the automower start/stop state."""
        if self.is_on:
            self.turn_off()
        else:
            self.turn_on()

    def stop(self, **kwargs):
        """Stop the automower (alias for turn_off)."""
        self.turn_off()

    def return_to_base(self, **kwargs):
        """Park the automower."""
        _LOGGER.debug("Sending PARK command to: %s", self._name)
        self._api.control("PARK")
        self._mower_status = STATUS_EXECUTING_PARK
        self.schedule_update_ha_state()

    def set_see(self, see):
        self._see = see

    def update(self):
        """Update the automower state using the API."""
        _LOGGER.debug("Fetching state from API: %s", self._name)
        self._state = self._api.status()

        # Do not update internal mower status and timestamp if
        # stored timestamp equals the one we last saw.
        # This allows for our internal STATUS_EXECUTING_* to
        # remain active until there's an actual change from the
        # API.
        if self._stored_timestamp != self._state["storedTimestamp"]:
            self._mower_status = self._state["mowerStatus"]
            self._stored_timestamp = self._state["storedTimestamp"]
        if self._see is not None:
            self.update_see()

    def update_see(self):
        """Update the device tracker."""
        _LOGGER.debug("Updating device tracker: %s", self._name)
        self._see(
            dev_id=self.dev_id,
            host_name=self.name,
            #            battery=self.battery,
            gps=(self.lat, self.lon),
            attributes={
                "status": self.status,
                "id": self.dev_id,
                "name": self.name,
                CONF_ICON: self.icon,
                "vendor": VENDOR,
                "model": self.model,
            },
        )
