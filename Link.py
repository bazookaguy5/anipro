import Database
import Global
import os.path
from os import system

class Link():
	
	def __init__(self, name, addr):
		# The splitted name: format ['Overlord', 'III', 'Episode', '8']
		name = Global.remove_extras( Global.normalize_characters(name) ) #normalizing in case of anomolous characters
		splitted_name = name.split(" ")

		if (splitted_name[-2] == "Episode"):
			episode_number = splitted_name.pop(-1) # Pops off the epsiode number from the end
			splitted_name.pop(-1) # REmoving the 'Episode' string from the end
		else:
			episode_number = "0"

		self.raw_name = name
		self.title = " ".join(splitted_name)
		self.name = "_".join(splitted_name)
		self.address = "" #This will be assigned by each child class
		self.episode_no = int(episode_number) if self.can_be_int(episode_number) else float(episode_number)
		self.list_type = Database.in_list(self.name)
	
	def _get_download_link(self, address): #an empty function that need to be overrided
		return 0 

	def download(self): #returns true or false wether the download was succesful or not

		download_link = self._get_download_link(self.address)
		
		if download_link == "":
			return False

		#If directory for the anime doesnt exist, creating it:
		if not os.path.exists(Global.save_directory + '\\' + self.title):
			system("mkdir \"" + Global.save_directory + '\\' + self.title + "\"")
			
		idm_command = 'idman.exe -d "' + download_link+ '" -p "' + Global.save_directory + '\\' + self.title + '" -f "' + self.raw_name + '.mp4"' + ' -n'
		system(idm_command)

		return True

	def can_be_int(self, str_):
		try:
			int(str_)
			return True
		except:
			return False