"""Constants for the Automower integration."""

DOMAIN = "automower"
DEFAULT_ICON = 'mdi:robot-mower'
VENDOR = "Husqvarna"
VACUUM_SCAN_INTERVAL = 60

from homeassistant.components.vacuum import (
    SUPPORT_BATTERY, SUPPORT_PAUSE, SUPPORT_RETURN_HOME,
    SUPPORT_STATUS, SUPPORT_STOP, SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON)

# TODO: Add more statuses as we observe them
STATUS_ERROR = 'ERROR'
STATUS_OK_CHARGING = 'OK_CHARGING'
STATUS_OK_CUTTING = 'OK_CUTTING'
STATUS_OK_CUTTING_MANUAL = 'OK_CUTTING_NOT_AUTO'
STATUS_OK_LEAVING = 'OK_LEAVING'
STATUS_OK_SEARCHING = 'OK_SEARCHING'
STATUS_PARKED_TIMER = 'PARKED_TIMER'
STATUS_PARKED_AUTOTIMER = 'PARKED_AUTOTIMER'
STATUS_PARKED_PARKED_SELECTED = 'PARKED_PARKED_SELECTED'
STATUS_PAUSED = 'PAUSED'
STATUS_EXECUTING_PARK = 'EXECUTING_PARK'
STATUS_EXECUTING_START = 'EXECUTING_START'
STATUS_EXECUTING_STOP = 'EXECUTING_STOP'
STATUS_OFF_HATCH_OPEN = 'OFF_HATCH_OPEN'
STATUS_OFF_HATCH_CLOSED = 'OFF_HATCH_CLOSED_DISABLED'
STATUS_OFF_DISABLED = 'OFF_DISABLED'

STATUSES = {
    STATUS_ERROR:                   { 'icon': 'mdi:alert',          'message': 'Error' },
    STATUS_OK_CHARGING:             { 'icon': 'mdi:power-plug',     'message': 'Charging' },
    STATUS_OK_CUTTING:              { 'icon': DEFAULT_ICON,         'message': 'Cutting' },
    STATUS_OK_CUTTING_MANUAL:       { 'icon': DEFAULT_ICON,         'message': 'Cutting (manual timer override)' },
    STATUS_OK_LEAVING:              { 'icon': DEFAULT_ICON,         'message': 'Leaving charging station' },
    STATUS_PAUSED:                  { 'icon': 'mdi:pause',          'message': 'Paused' },
    STATUS_PARKED_TIMER:            { 'icon': 'mdi:timetable',      'message': 'Parked due to timer' },
    STATUS_PARKED_AUTOTIMER:        { 'icon': 'mdi:timetable',      'message': 'Parked due to weather timer' },
    STATUS_PARKED_PARKED_SELECTED:  { 'icon': 'mdi:sleep',          'message': 'Parked manually' },
    STATUS_OK_SEARCHING:            { 'icon': 'mdi:magnify',        'message': 'Going to charging station' },
    STATUS_EXECUTING_START:         { 'icon': 'mdi:dots-horizontal','message': 'Starting...' },
    STATUS_EXECUTING_STOP:          { 'icon': 'mdi:dots-horizontal','message': 'Stopping...' },
    STATUS_EXECUTING_PARK:          { 'icon': 'mdi:dots-horizontal','message': 'Preparing to park...' },
    STATUS_OFF_HATCH_OPEN:          { 'icon': 'mdi:alert',          'message': 'Hatch opened' },
    STATUS_OFF_HATCH_CLOSED:        { 'icon': 'mdi:pause',          'message': 'Stopped but not on base' },
    STATUS_OFF_DISABLED:            { 'icon': 'mdi:close-circle-outline', 'message': 'Off'}
}

# TODO: Add more error messages as we observe them
ERROR_MESSAGES = {
    1:  'Outside working area',
    2:  'No loop signal',
    9:  'Trapped',
    10: 'Upside down',
    12: 'Empty battery',
    13: 'No drive',
    25: 'Cutting system blocked'
}

# TODO: Add more models as we observe them
MODELS = {
    'E': 'Automower 420',
    'G': 'Automower 430X',
    'H': 'Automower 450X',
    'K': 'Automower 310',
    'L': 'Automower 315/X'
}

IGNORED_API_STATE_ATTRIBUTES = [
    'batteryPercent',
    'cachedSettingsUUID',
    'lastLocations',
    'mowerStatus',
    'valueFound'
]

SUPPORTED_FEATURES = SUPPORT_TURN_ON | SUPPORT_TURN_OFF | SUPPORT_PAUSE | \
                     SUPPORT_STOP | SUPPORT_RETURN_HOME | \
                     SUPPORT_STATUS | SUPPORT_BATTERY



