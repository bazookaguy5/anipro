from ggsh import ggsh_link

while True:
	link = input()
	episode = ggsh_link("Kobayashi-san Chi no Maid Dragon Episode 2", link)
	episode.download()

# from ggto import ggto_link

# while True:
	# link = input()
	# episode = ggto_link("Anime Episode 8", link)
	# episode.download()
	