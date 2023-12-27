from tkinter import *

window = Tk()
window.title("Carlos' GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Create a label
my_label = Label(text="I am a label", font=("times new roman", 24))
# my_label.pack()  # pack is used to show the label on the screen instead of the console and center it.
# my_label.place(x=210, y=110)  # place is used to show the label on the screen instead of the console. Downside is that
# it is too specific and we need to figure out the x and y coordinates.
my_label.grid(column=0, row=0)


# buttons
def button_clicked():
    print("I got clicked")
    new_text = inputter.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New button")
# new_button.pack()
new_button.grid(column=2, row=0)

# Entry/Input
inputter = Entry(width=10)  # width is used to set the width of the entry in the parent
# inputter.pack()
inputter.grid(column=3, row=3)  # grid is used to show the entry on the screen. You cannot use pack with grid.

window.mainloop()  # main loop is used to keep the window open