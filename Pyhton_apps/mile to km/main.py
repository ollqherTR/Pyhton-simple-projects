from tkinter import *
window = Tk()
window.title("Miles to kilometer converter")

miles_input = Entry()
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal = Label(text="is equal to ")
is_equal.grid(column=0,row=1)

kilometer_resoult = Label(text="0")
kilometer_resoult.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

clc_button = Button(text="Calculate")
clc_button.grid(column=1,row=2)