import os
from helpers import is_command_result_successfull, get_filenames, is_python_source, find_commands_at_file
from logging import print_info, print_success, print_error, print_warning

class Status:
	UNKNOWN = 'UNKNOWN'
	SUCCESS = 'SUCCESS'
	ERROR = 'ERROR'

class Test:
	def __init__(self, filename, command):
		self.filename = filename
		self.command = command
		self.status = Status.UNKNOWN

	@staticmethod
	def collect_tests(path='.'):
		print_info('Collecting tests...')

		all_filenames = get_filenames(path)

		tests = []
		for filename in all_filenames:
			path_to_file = os.path.join(path, filename)
			if not is_python_source(filename):
				continue

			print_info('Searching at {}...'.format(filename))
			commands = find_commands_at_file(path_to_file)

			if not len(commands):
				print_warning('No test commands for {}'.format(filename))
				continue

			print_info('{} command was found:'.format(len(commands)))
			for current_command in commands:
				print_info('command: {}'.format(current_command))
				tests.append(Test(path_to_file, current_command))

		return tests

	@staticmethod
	def run_tests(tests):
		for test in tests:
			test.run()

	@staticmethod
	def get_failed_tests(tests):
		failed_tests = []
		for test in tests:
			if test.status == Status.ERROR:
				failed_tests.append(test)
		return failed_tests

	def __str__(self):
		return '{} ({}, {})'.format(self.status, self.filename, self.command)

	def run(self):
		print_info('RUNNING TEST: {} ({})'.format(self.filename, self.command))
		result = os.system(self.command)
		if is_command_result_successfull(result):
			print_success('SUCCESS')
			self.status = Status.SUCCESS
		else:
			print_error('ERROR: {}'.format(result))
			self.status = Status.ERROR
