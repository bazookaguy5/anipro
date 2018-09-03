from ggto import ggto_link

while True:
	link = input()
	episode = ggto_link("Anime Episode 8", link)
	episode.download()
	