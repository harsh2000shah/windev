# importing shits....
from tkinter import *
import os as os


# create a root object... like body in html
root = Tk()

# title just like the html thingie... and icon... near the title...
root.title("AaplaHR | Register")
icon_photo = PhotoImage(file ="logistics64.png")
root.iconphoto(False, icon_photo)

#****************************   VARIABLES ********************************



#****************************   FUNCTIONS ********************************





# the company logo...
photo = PhotoImage(file="image.png")
label = Label(root, image=photo, height=100, bg="#00BFFF").pack(fill="both", expand=True, ipady=(20), ipadx=(50))

canvas = Canvas(root, height=300, width=500, highlightthickness=0, bg="#00BFFF")
frame = Frame(canvas, height=400, width=400, bg="white").pack()
#******************************************************************************************************





#******************************************************************************************************
canvas.pack(fill="both", expand=True)

# run forever!
root.mainloop()
