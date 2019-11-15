from HTMLGet import Connection
import Link

class ggto_link(Link.Link):

	link_no = 1

	def __init__(self, name, addr):
		super().__init__(name, addr)
		self.address = addr

	def _get_download_link(self, link):
		page1_cnc = Connection(link)
		page1_links = page1_cnc.get_from_tag("//div/div/p/iframe/@src")
		page2_cnc = Connection(page1_links[self.link_no])

		# because of js page generation for the second site, xpath cannot properly be used to get the links. hence i use my own parser:
		lines = page2_cnc.get_content().decode().split("\n")
		for line in lines:
			if "file: \"http://" in line:
				download_link = line.split('"')[1]
				return download_link


def create_list():
	connection = Connection("http://www.gogoanime.to") #Creating a connection to the main page	
	released_anime = []

	list_of_names = connection.get_from_tag("//td[@class='redgr']/ul/li/a/text()[1]")
	list_of_addrs = connection.get_from_tag("//td[@class='redgr']/ul/li/a/@href")

	# Creating a list of ggto_link objects
	# The format for the dictionary is {'The First Anime Episode 3': ("The_First_Anime", "http://anime.link/here", '3', 'pref_list')}
	for name, addr in zip(list_of_names, list_of_addrs):
		released_anime.append( ggto_link(name, addr) )

	return released_anime