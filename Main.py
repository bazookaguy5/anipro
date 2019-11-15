import Database
from HTMLGet import Connection
import Global

if Global.site == 2:
	from ggto import create_list
else:
	from ggsh import create_list


def download_cmd():
	released_anime = create_list()

	for anime in released_anime:
		if anime.list_type == 'pref_list':
			if ( anime.episode_no > Database.pref_anime[anime.name] ):  # Checking if the episode number of the released anime is newer than what i had previously downloaded
				print("Downloading", anime.name)
				downloaded = anime.download()
				if downloaded:
					Database.increment(anime.name, anime.episode_no)
					
		elif anime.list_type == False:
			print("\nThe anime " + anime.name + " is not in any list")
			print("Which list should it be added to?:")
			print("1.Preference List\n2.Black List\n")
			input_ = input()

			if input_ == '1':
				Database.add_to_whitelist(anime)
				print("Download now? (y/n):")
				input_ = input()

				if input_ == 'y':
					anime.download()

			elif input_ == '2':
				Database.add_to_blacklist(anime)

if __name__ == "__main__":
	download_cmd()

# tree.xpath("//div[@id='videoDownload']//td/a/@href'")   aaa
