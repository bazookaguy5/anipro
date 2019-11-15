
import Global
from multiprocessing import Process
import Database
from threading import Thread
import time
from tkinter import Frame, Label, Listbox, Menu, Text, Tk 
from tkinter import END, EXTENDED, HORIZONTAL, INSERT
from tkinter.ttk import Button, Separator
if Global.site == 2:
	from ggto import create_list
else:
	from ggsh import create_list


class MainWindow(Frame):

	def __init__(self, master=None):
		self.released_anime = []

		Frame.__init__(self, master)
		
		self.grid()
		self.createWidgets()
		#master.resizable(False, False) #making the window un-resizable
		master.config(menu=self.menubar)

	def createWidgets(self):
		# The menu bar at the top
		self.menubar = Menu(self) 

		# The submenu of the menubar
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="Open")
		self.menubar.add_cascade( label = "File", menu = self.filemenu)

		# The list that will contain all the anime names
		self.list = Listbox(self, width=50, selectmode=EXTENDED)
		self.list.grid(row=0, column=0, rowspan=2)

		# The button that generates the listing
		self.list_button = Button(self, text="Create list", command=lambda: self.generate_list() )
		self.list_button.grid(row=0, column=1)

		# The button that generates the listing
		self.list_and_download_button = Button(self, text="Create & download list", 
											command=lambda: self.generate_and_download_list() )
		self.list_and_download_button.grid(row=1, column=1)

		# The button that downloads the selected items
		self.download_button = Button(self, text="Download", command=lambda: self.download_selected())
		self.download_button.grid(row=2, column=1)

		#seperator in the middle
		self.seperator = Separator(orient=HORIZONTAL)
		self.seperator.grid(row=3, column=0, pady=5, padx=20, columnspan=2, sticky="ew")

		#Log box at the bottom
		self.log_box = Text( width=57, height=14, bg="silver")
		self.log_box.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

	def generate_list(self):
		self.log("Creating List...")
		self.released_anime = create_list()

		for anime in self.released_anime:
			self.list.insert(END, anime.raw_name)
		self.log("List made!")

	def generate_and_download_list(self):
		self.generate_list()

		for anime in self.released_anime:
			if anime.list_type == 'pref_list':
				if ( anime.episode_no > Database.pref_anime[anime.name] ):  # Checking if the episode number of the released anime is newer than what i had previously downloaded	
					self.log("Downloading " + anime.title)
					downloaded = anime.download()
					if downloaded:
						Database.increment(anime.name, anime.episode_no)
			elif anime.list_type == False:
				AddAnimeDialog(anime, Tk()).mainloop()
		self.log("Done!")

	def download_selected(self):
		for index in self.list.curselection():
			self.log(f"Downloading {self.released_anime[index].title}")
			self.released_anime[index].download()

	def log(self, message):
		self.log_box.insert(INSERT, message + "\n")
		time.sleep(0.1)



class AddAnimeDialog(Frame):
	
	def __init__(self, anime, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.anime = anime
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		#The text in the prompt
		self.prompt = Label(self, text=f"\nThe anime {self.anime.name} is not in any list\nWhich list should it be added to?")
		self.prompt.grid(row=0, column=0, columnspan=3)

		#The whitelist (preference list) button
		self.whitelist_button = Button(self, text="White list", command=lambda: self.add_to_whitelist() )
		self.whitelist_button.grid(row=1, column=0)

		#The whitelist (preference list) button
		self.blacklist_button = Button(self, text="Black list", command=lambda: self.add_to_blacklist() )
		self.blacklist_button.grid(row=1, column=1)

		#The whitelist (preference list) button
		self.cancel_button = Button(self, text="Cancel", command=lambda: self.master.destroy())
		self.cancel_button.grid(row=1, column=2)

	def add_to_whitelist(self):
		Database.add_to_whitelist(self.anime)
		self.master.destroy()

	def add_to_blacklist(self):
		Database.add_to_blacklist(self.anime)
		self.master.destroy()

root = Tk()
window = MainWindow(master=root)
window.mainloop()