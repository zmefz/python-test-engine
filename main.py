from logging import print_error, print_success, set_log_level, print_info
from config import default_log_level
from test import Test

def start_tests(path='.', log_level=default_log_level):
	"""
		Function to run tests at chosen directory
		Params:
			path: string 		- path to chosen directory
			log_level?: string 	- one of ERROR, WARNING, INFO, SUCCESS
				The system logs messages with level not bigger than chosen log_level.
				For example if chosen level is WARNING - the system will show ERROR
				and WARNING messages.
	"""

	set_log_level(log_level)

	print_info('Starting...')
	tests = Test.collect_tests(path)
	Test.run_tests(tests)
	failed_tests = Test.get_failed_tests(tests)
	print_info('Finished!')

	if len(failed_tests):
		print_error('Not all tests successfully passed :(')
		print_error('Failed tests:')
		for test in failed_tests:
			print_error(test)
	else:
		print_success('All tests successfully pased!')
