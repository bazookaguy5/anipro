import Database
from HTMLGet import Connection
from os import system

class ggto_link():

	link_no = 1

	def __init__(self, name, addr):
		# The splitted name: format ['Overlord', 'III', 'Episode', '8']
		splitted_name = name.split(" ")

		if (splitted_name[-2] == "Episode"):
			episode_number = splitted_name.pop(-1) # Pops off the epsiode number from the end
			splitted_name.pop(-1) # REmoving the 'Episode' string from the end
		else:
			episode_number = "0"

		self.raw_name = name
		self.name = "_".join(splitted_name)
		self.address = addr
		self.episode_no = int(episode_number)
		self.list_type = Database.in_list(self.name)


	def download(self):
		print("Downloading", self.name)

		download_link = self.__get_download_link(self.address)
		idm_command = 'idman.exe -d "' + str(download_link, 'utf-8') + '"'
		system(idm_command)

	def __get_download_link(self, link):
		page1_cnc = Connection(link)
		page1_links = page1_cnc.get_from_tag("//div/div/p/iframe/@src")
		page2_cnc = Connection(page1_links[self.link_no])

		# because of js page generation for the second site, xpath cannot properly be used to get the links. hence i use my own parser:
		lines = page2_cnc.get_content().split(b'\n')
		for line in lines:
			if b"file: \"http://" in line:
				download_link = line.split(b'"')[1]
				return download_link


def create_list_ggto():
	connection = Connection("http://www.gogoanime.to") #Creating a connection to the main page	
	released_anime = []

	list_of_names = connection.get_from_tag("//td[@class='redgr']/ul/li/a/text()")
	list_of_addrs = connection.get_from_tag("//td[@class='redgr']/ul/li/a/@href")

	# Creating a list of ggto_link objects
	# The format for the dictionary is {'The First Anime Episode 3': ("The_First_Anime", "http://anime.link/here", '3', 'pref_list')}
	for name, addr in zip(list_of_names, list_of_addrs):
		released_anime.append( ggto_link(name, addr) )

	return released_anime
