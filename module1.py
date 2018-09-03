#import Main
from tkinter import Tk, Frame, Listbox, Menu
from tkinter.ttk import Button

class MainWindow(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master, width=500, height=500)
		self.place()
		self.createWidgets()
		master.resizable(False, False)
		master.config(menu=self.menubar)

	def createWidgets(self):
		self.button = Button(self, text="what")#, command=self.generate_list(Main.create_list()))
		self.button.place(x=100, y=100)

		# The list that will contain all the anime names
		self.list = Listbox(self)
		self.list.insert(-1, "b")
		self.list.place( x=20, y=20)

		# The menu bar at the top
		self.menubar = Menu(self)
		
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="Open")
		self.menubar.add_cascade( label = "File", menu = self.filemenu)

	# def generate_list(self, lists):
	# 	for anime in lists:
	# 		self.list.insert(-1, anime.raw_name)



root = Tk()

window = MainWindow(master=root)
window.mainloop()