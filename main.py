# Bhimisti-Software
from Tkinter import *
import tkFileDialog

root = Tk()

def open_file():

def save_file():



menu = Menu(root)


fileMenu = Menu(menu,tearoff=0)
fileMenu.add_command(label="Open",command=open_file)
fileMenu.add_command(label="Save",command=save_file)
