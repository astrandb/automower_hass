"""Constants for the Automower integration."""

from homeassistant.components.vacuum import (
    SUPPORT_BATTERY,
    SUPPORT_PAUSE,
    SUPPORT_RETURN_HOME,
    SUPPORT_STATUS,
    SUPPORT_STOP,
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,
)

DOMAIN = "automower"
DEFAULT_ICON = "mdi:robot-mower"
VENDOR = "Husqvarna"
VACUUM_SCAN_INTERVAL = 60
VERSION = "0.5.1"

# TODO: Add more statuses as we observe them
STATUS_ERROR = "ERROR"
STATUS_OK_CHARGING = "OK_CHARGING"
STATUS_OK_CUTTING = "OK_CUTTING"
STATUS_OK_CUTTING_MANUAL = "OK_CUTTING_NOT_AUTO"
STATUS_OK_LEAVING = "OK_LEAVING"
STATUS_OK_SEARCHING = "OK_SEARCHING"
STATUS_PARKED_TIMER = "PARKED_TIMER"
STATUS_PARKED_AUTOTIMER = "PARKED_AUTOTIMER"
STATUS_PARKED_PARKED_SELECTED = "PARKED_PARKED_SELECTED"
STATUS_PAUSED = "PAUSED"
STATUS_EXECUTING_PARK = "EXECUTING_PARK"
STATUS_EXECUTING_START = "EXECUTING_START"
STATUS_EXECUTING_STOP = "EXECUTING_STOP"
STATUS_WAIT_POWER_UP = "WAIT_POWER_UP"
STATUS_OFF_HATCH_OPEN = "OFF_HATCH_OPEN"
STATUS_OFF_HATCH_CLOSED = "OFF_HATCH_CLOSED_DISABLED"
STATUS_OFF_DISABLED = "OFF_DISABLED"

STATUSES = {
    STATUS_ERROR: {"icon": "mdi:alert", "message": "Error"},
    STATUS_OK_CHARGING: {"icon": "mdi:battery-charging", "message": "Charging"},
    STATUS_OK_CUTTING: {"icon": DEFAULT_ICON, "message": "Mowing"},
    STATUS_OK_CUTTING_MANUAL: {
        "icon": DEFAULT_ICON,
        "message": "Mowing (manual timer override)",
    },
    STATUS_OK_LEAVING: {"icon": DEFAULT_ICON, "message": "Leaving charging station"},
    STATUS_PAUSED: {"icon": "mdi:pause", "message": "Paused"},
    STATUS_PARKED_TIMER: {"icon": DEFAULT_ICON, "message": "Parked (week timer)"},
    STATUS_PARKED_AUTOTIMER: {
        "icon": "mdi:weather-partly-cloudy",
        "message": "Parked (weather timer)",
    },
    STATUS_PARKED_PARKED_SELECTED: {"icon": "mdi:garage", "message": "Parked (manual)"},
    STATUS_OK_SEARCHING: {
        "icon": "mdi:magnify",
        "message": "Going to charging station",
    },
    STATUS_EXECUTING_START: {"icon": "mdi:dots-horizontal", "message": "Starting..."},
    STATUS_EXECUTING_STOP: {"icon": "mdi:dots-horizontal", "message": "Stopping..."},
    STATUS_WAIT_POWER_UP: {"icon": "mdi:dots-horizontal","message": "Powering up..."},
    STATUS_EXECUTING_PARK: {
        "icon": "mdi:dots-horizontal",
        "message": "Preparing to park...",
    },
    STATUS_OFF_HATCH_OPEN: {"icon": "mdi:alert", "message": "Hatch opened"},
    STATUS_OFF_HATCH_CLOSED: {
        "icon": "mdi:pause",
        "message": "Stopped but not on base",
    },
    STATUS_OFF_DISABLED: {"icon": "mdi:close-circle-outline", "message": "Off"},
}

# TODO: Add more error messages as we observe them
ERROR_MESSAGES = {
	0: 'Unexpected error',
	1: 'Outside working area',
	2: 'No loop signal',
	3: 'Wrong loop signal',
	4: 'Loop sensor problem, front',
	5: 'Loop sensor problem, rear',
	6: 'Loop sensor problem, left',
	7: 'Loop sensor problem, right',
	8: 'Wrong PIN code',
	9: 'Trapped',
	10: 'Upside down',
	11: 'Low battery',
	12: 'Empty battery',
	13: 'No drive',
	14: 'Mower lifted',
	15: 'Lifted',
	16: 'Stuck in charging station',
	17: 'Charging station blocked',
	18: 'Collision sensor problem, rear',
	19: 'Collision sensor problem, front',
	20: 'Wheel motor blocked, right',
	21: 'Wheel motor blocked, left',
	22: 'Wheel drive problem, right',
	23: 'Wheel drive problem, left',
	24: 'Cutting system blocked',
	25: 'Cutting system blocked',
	26: 'Invalid sub-device combination',
	27: 'Settings restored',
	28: 'Memory circuit problem',
	29: 'Slope too steep',
	30: 'Charging system problem',
	31: 'STOP button problem',
	32: 'Tilt sensor problem',
	33: 'Mower tilted',
	34: 'Cutting stopped - slope too steep',
	35: 'Wheel motor overloaded, right',
	36: 'Wheel motor overloaded, left',
	37: 'Charging current too high',
	38: 'Electronic problem',
	39: 'Cutting motor problem',
	40: 'Limited cutting height range',
	41: 'Unexpected cutting height adj',
	42: 'Limited cutting height range',
	43: 'Cutting height problem, drive',
	44: 'Cutting height problem, curr',
	45: 'Cutting height problem, dir',
	46: 'Cutting height blocked',
	47: 'Cutting height problem',
	48: 'No response from charger',
	49: 'Ultrasonic problem',
	50: 'Guide 1 not found',
	51: 'Guide 2 not found',
	52: 'Guide 3 not found',
	53: 'GPS navigation problem',
	54: 'Weak GPS signal',
	55: 'Difficult finding home',
	56: 'Guide calibration accomplished',
	57: 'Guide calibration failed',
	58: 'Temporary battery problem',
	59: 'Temporary battery problem',
	60: 'Temporary battery problem',
	61: 'Temporary battery problem',
	62: 'Temporary battery problem',
	63: 'Temporary battery problem',
	64: 'Temporary battery problem',
	65: 'Temporary battery problem',
	66: 'Battery problem',
	67: 'Battery problem',
	68: 'Temporary battery problem',
	69: 'Alarm! Mower switched off',
	70: 'Alarm! Mower stopped',
	71: 'Alarm! Mower lifted',
	72: 'Alarm! Mower tilted',
	73: 'Alarm! Mower in motion',
	74: 'Alarm! Outside geofence',
	75: 'Connection changed',
	76: 'Connection NOT changed',
	77: 'Com board not available',
	78: 'Slipped - Mower has Slipped.Situation not solved with moving pattern',
	79: 'Invalid battery combination - Invalid combination of different battery types.',
	80: 'Cutting system imbalance: Warning',
	81: 'Safety function faulty',
	82: 'Wheel motor blocked, rear right',
	83: 'Wheel motor blocked, rear left',
	84: 'Wheel drive problem, rear right',
	85: 'Wheel drive problem, rear left',
	86: 'Wheel motor overloaded, rear right',
	87: 'Wheel motor overloaded, rear left',
	88: 'Angular sensor problem',
	89: 'Invalid system configuration',
	90: 'No power in charging station',
}

# TODO: Add more models as we observe them
MODELS = {
    "E": "Automower 420",
    "G": "Automower 430X",
    "H": "Automower 450X",
    "K": "Automower 310",
    "L": "Automower 315/X",
}

IGNORED_API_STATE_ATTRIBUTES = [
    "batteryPercent",
    "cachedSettingsUUID",
    "lastLocations",
    "mowerStatus",
    "valueFound",
]

SUPPORTED_FEATURES = (
    SUPPORT_TURN_ON
    | SUPPORT_TURN_OFF
    | SUPPORT_PAUSE
    | SUPPORT_STOP
    | SUPPORT_RETURN_HOME
    | SUPPORT_STATUS
    | SUPPORT_BATTERY
)
