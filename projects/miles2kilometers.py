from tkinter import *

window = Tk()
window.title("Miles to kilometers converter")
window.minsize(width=500, height=300)

miles_input = Entry()

miles_label = Label(text="Miles")

is_equal_label = Label(text="is equal to")

window.mainloop()
