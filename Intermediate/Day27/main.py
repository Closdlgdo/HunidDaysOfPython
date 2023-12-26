from tkinter import *

window = Tk()
window.title("Carlos' GUI")
window.minsize(width=500, height=300)

# Create a label
my_label = Label(text="I am a label", font=("times new roman", 24))
my_label.pack()  # pack is used to show the label on the screen instead of the console and center it.


# buttons
def button_clicked():
    print("I got clicked")


button = Button(text="Click me", command=button_clicked)
button.pack()










window.mainloop()  # main loop is used to keep the window open