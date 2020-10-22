"""Vacuum for Husqvarna Automowers"""

from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Husqvarna Automower sensor platform."""
    async_add_entities(hass.data[DOMAIN]['entities'])