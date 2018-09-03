#import Downloader
#import Global
import Database
from HTMLGet import Connection
from ggto import create_list_ggto
from ggsh import create_list_ggsh

#gets The list of names and addreses of currently released anime


def download_cmd():
	# Now deciding what do with each name based on what list it is in:
	released_anime = create_list_ggsh()

	for anime in released_anime:
		if anime.list_type == 'pref_list':
			if ( anime.episode_no > Database.pref_anime[anime.name] ):  # Checking if the episode number of the released anime is newer than what i had previously downloaded
				anime.download()
				Database.increment(anime.name, anime.episode_no)
		elif anime.list_type == False:
			print ("fff")
			Database.add_to_list(anime)

if __name__ == "__main__":
	download_cmd()

# tree.xpath("//div[@id='videoDownload']//td/a/@href'")   aaa
