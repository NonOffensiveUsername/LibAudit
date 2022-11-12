import tkinter as tk
from interface import Interface
from id_manager import IDManager

print("Creating Window")
window = tk.Tk()

manager = IDManager()

print("Initializing Interface")
app = Interface(window, manager, None)

print("Exiting")