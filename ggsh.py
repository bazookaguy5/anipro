import Database
from HTMLGet import Connection
from os import system

class ggsh_link():

	#link_no = 1

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
		self.address = "https://www1.gogoanime.sh" + addr
		self.episode_no = int(episode_number)
		self.list_type = Database.in_list(self.name)


	def download(self):
		print("Downloading", self.name)

		download_link = self.__get_download_link(self.address)
		idm_command = 'idman.exe -d "' + download_link + '"'
		system(idm_command)

	def __get_download_link(self, link):
		page1_cnc = Connection(link)

		page1_links = page1_cnc.get_from_tag("//div[2]/div[3]/a/@href")
		page2_cnc = Connection(page1_links[0])

		final_link = page2_cnc.get_from_tag("//div[2]/div/div[4]/div/a/@href")
		#/html/body/section/div/div[2]/div/div[4]/div/a
		return final_link[0]


def create_list_ggsh():
	connection = Connection("http://www.gogoanime.sh") #Creating a connection to the main page	
	released_anime = []

	list_of_names = connection.get_from_tag("//p/a/@title")
	list_of_episode_nums = connection.get_from_tag("//li/p/text()")
	list_of_addrs = connection.get_from_tag("//p/a/@href")

	# Creating a list of ggto_link objects
	# The format for the dictionary is {'The First Anime Episode 3': ("The_First_Anime", "http://anime.link/here", '3', 'pref_list')}
	for name, ep_num, addr in zip(list_of_names, list_of_episode_nums, list_of_addrs):
		released_anime.append( ggsh_link(name + " " + ep_num, addr) )

	return released_anime

	
