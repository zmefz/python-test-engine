import os
from config import py_ext, command_line_starts_with

def find_commands_at_file(filename):
	commands = []
	with open(filename, 'r') as f:
		for line in f.readlines():
			if line.startswith(command_line_starts_with):
				commands.append(get_command_from_line(line))
	return commands

def get_command_from_line(line):
	return line[len(command_line_starts_with) + 1:-1]

def is_python_source(filename):
	_, ext = os.path.splitext(filename)
	return ext == py_ext

def get_filenames(path):
	path = os.path.abspath(path)
	items = os.walk(path)
	_, folders, filenames = next(items)
	return filenames

def is_command_result_successfull(result):
	return result == 0
