from HTMLGet import Connection
import Link
from os import system

class ggsh_link(Link.Link):

	#link_no = 1

	def __init__(self, name, addr):
		super().__init__(name, addr)
		self.address = "https://www9.gogoanime.io" + addr

	def _get_download_link(self, link):
		page1_cnc = Connection(link)
		page1_links = page1_cnc.get_from_tag("//div[1]/div[2]/div[1]/a[2]/@href")
		page2_cnc = Connection(page1_links[0])
		final_link = page2_cnc.get_from_tag("//div[2]/div/div[4]/div/a/@href")
		#/html/body/section/div/div[2]/div/div[4]/div/a

		#This next block is only for when only the mirror link section is populated
		if len(final_link) == 0:
			final_link = page2_cnc.get_from_tag("//div[2]/div/div[5]/div/a/@href")
			
			if len(final_link) == 0:
				return ""
				
			for address in final_link:
				if "rapidvideo" in address:
					second_vendor_cnc = Connection(address)
					second_vendor_link = second_vendor_cnc.get_from_tag("//div/span/a/@href")
					if len(second_vendor_link) == 0:
						return ""
					return second_vendor_link[0] #(second_vendor_link[0] if len(second_vendor_link) < 2 else second_vendor_link[1]) 

		return final_link[0]#(final_link[-2] if len(final_link) > 2 else final_link[-1]) 
	



def create_list():
	connection = Connection("https://www2.gogoanime.io/") #Creating a connection to the main page	
	released_anime = []

	list_of_names = connection.get_from_tag("//p/a/@title")
	list_of_episode_nums = connection.get_from_tag("//li/p/text()[1]")
	list_of_addrs = connection.get_from_tag("//p/a/@href")

	# Creating a list of ggto_link objects
	# The format for the dictionary is {'The First Anime Episode 3': ("The_First_Anime", "http://anime.link/here", '3', 'pref_list')}
	for name, ep_num, addr in zip(list_of_names, list_of_episode_nums, list_of_addrs):
		released_anime.append( ggsh_link(name + " " + ep_num, addr) )

	return released_anime
