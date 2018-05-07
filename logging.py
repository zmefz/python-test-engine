from config import default_log_level

class LOG_LEVEL:
	ERROR = 1
	WARNING = 2
	SUCCESS = 3
	INFO = 4

LOG_LEVEL.ACTIVE = LOG_LEVEL.WARNING

_LOG_LEVEL_STRINGS = {
	'ERROR': LOG_LEVEL.ERROR,
	'WARNING': LOG_LEVEL.WARNING,
	'SUCCESS': LOG_LEVEL.SUCCESS,
	'INFO': LOG_LEVEL.INFO,
}

class _PRINT_COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def _print_logs(message, level=LOG_LEVEL.INFO):
	if level > LOG_LEVEL.ACTIVE:
		return

	string_start = ''
	if level == LOG_LEVEL.INFO:
		string_start = '{}[INFO]'.format(_PRINT_COLORS.OKBLUE)
	elif level == LOG_LEVEL.WARNING:
		string_start = '{}[WARNING]'.format(_PRINT_COLORS.HEADER)
	elif level == LOG_LEVEL.ERROR:
		string_start = '{}[ERROR]'.format(_PRINT_COLORS.FAIL)
	elif level == LOG_LEVEL.SUCCESS:
		string_start = '{}[SUCCESS]'.format(_PRINT_COLORS.BOLD)
	else:
		raise ValueError('Invalid log level')

	print('{} {}{}'.format(string_start, message, _PRINT_COLORS.ENDC))

def print_warning(message):
	_print_logs(message, level=LOG_LEVEL.WARNING)

def print_success(message):
	_print_logs(message, level=LOG_LEVEL.SUCCESS)

def print_info(message):
	_print_logs(message, level=LOG_LEVEL.INFO)

def print_error(message):
	_print_logs(message, level=LOG_LEVEL.ERROR)

def set_log_level(new_log_level):
	try:
		LOG_LEVEL.ACTIVE = _LOG_LEVEL_STRINGS[new_log_level]
	except KeyError as e:
		print_error('Invalid log level: {}'.format(new_log_level))
		raise e

if default_log_level:
	set_log_level(default_log_level)
