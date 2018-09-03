#
# DatabaseManager module v1.2
# v1.2 : cleaned up the code a bit
# v1.1 : added support to create file if file does not exist
#		also added support for lists
#

from os import path, system


def data_export(data, type, filename):
	"""Stores data into a single string to place inside a file"""
	if not path.exists(filename):
		system("copy nul \"" + filename + "\"")

	file = open(filename, 'w')
	output_string = ""

	# For Dictionaries
	if type == 'dict':
		for key, val in zip(data.keys(), data.values()):
			output_string += key + "||" + str(val) + "}+{"
		output_string = output_string[:-3]

	# For Lists
	elif type == 'list':
		output_string = "||".join(data)

	file.write(output_string)
	file.close()


def data_import(type, filename):
	"""exports data so that it can be used. converts the data that has been made into a string by data_export"""
	if not path.exists(filename):
		system("copy nul \"" + filename + "\"") #because i need a file even if empty

	file = open(filename)
	file_data = file.read()

	# For Dictionaries
	if type == 'dict':
		if file_data == "":
			return {}
		else:
			output_dict = {}
			pairs = file_data.split("}+{")
			for pair in pairs:
				key_value = pair.split("||")
				output_dict[key_value[0]] = int(key_value[1])
			file.close()
			return output_dict

	# For Lists
	elif type == 'list':
		output_list = file_data.split("||")
		return output_list