"""Vacuum for Husqvarna Automowers"""
from datetime import timedelta

from .const import DOMAIN, VACUUM_SCAN_INTERVAL

SCAN_INTERVAL = timedelta(seconds=VACUUM_SCAN_INTERVAL)


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Husqvarna Automower sensor platform."""
    async_add_entities(hass.data[DOMAIN]["entities"])
