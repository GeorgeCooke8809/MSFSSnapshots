from tkinter import *
import tkinter
import Functions

colour_one = "#bfd2ff"
contrast_one = "#000000"
colour_two = "#01104d"
contrast_two = "#FFFFFF"

fonts = ("Monoton", 20, "bold")

def func_save_button():
    Functions.save_location()

def func_load_button():
    Functions.set_location()

root = Tk()
root.title("MSFS Snapshot Tool")
root.geometry("400x150")

frame = tkinter.Frame(root)

frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 1)

frame.rowconfigure(0, weight = 1)

save_button = tkinter.Button(frame, text = "                         \nSave Position\n                         ", command = func_save_button, bg = colour_one, fg = contrast_one, borderwidth = 0, font = fonts)
save_button.grid(row = 0, column = 0, sticky = "nsew")

load_button = tkinter.Button(frame, text = "                         \nLoad Last\nSnapshot\n                         ", command = func_load_button, bg = colour_two, fg = contrast_two, borderwidth = 0, font = fonts)
load_button.grid(row = 0, column = 1, sticky = "nsew")

frame.pack(fill = "both", expand = True)

root.mainloop()
