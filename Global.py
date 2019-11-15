#functions and variables used by most of the files

site = 1 #the site to use, (1)the sd gg (2)the hd gg
save_directory = "D:\\Anime"

def normalize_characters (text):
	for char in text:
		if ord(char) < 32 or ord(char) > 126:
			text = text.replace(char, '')
	
	return text
	
def remove_extras(text):
	for char in text:
		if char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
			text = text.replace(char, ' ')
	
	return text