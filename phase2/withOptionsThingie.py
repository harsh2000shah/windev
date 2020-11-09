# !/usr/bin/python3
# importing shits....
from tkinter import *
# create a root object... like body in html
root = Tk()

# title just like the html thingie... and icon... near the title...
root.title("AaplaHR | Register")
icon_photo = PhotoImage(file="logistics64.png")
root.iconphoto(False, icon_photo)

# ****************************   VARIABLES ********************************
var = IntVar()
var_radio = "Please select one of the below to Upload:-"

# ****************************   FUNCTIONS ********************************
def callback():
    if var.get() == 1:
        var_radio = "Click Upload button to upload Excel file"
        shit = select()


    else:
        var_radio = "Click Upload button to upload CSV file"
    label.config(canvas, text=var_radio)
    print(var_radio)

# the company picture...
photo = PhotoImage(file="image.png")
label_photo = Label(root, image=photo, height=100, bg="#00BFFF").pack(fill="both", expand=True, ipady=20, ipadx=50)

canvas = Canvas(root, height=0, width=0, highlightthickness=0, bd=0, bg="#00BFFF").pack()

label = Label(canvas, text=var_radio, bg="#00BFFF", fg="white", font=('calibre', 14, 'bold'))
label.pack(fill="both", expand=True, ipady=10)
R1 = Radiobutton(canvas, text="Excel", variable=var, value=1, fg="white", font=('calibre', 11, 'bold'), command=callback, bg="#00BFFF").pack(fill="both", expand=True, ipady=5)
R2 = Radiobutton(canvas, text="CSV", variable=var, value=2,  fg="white", font=('calibre', 11, 'bold'), command=callback, bg="#00BFFF").pack(fill="both", expand=True, ipady=5)

# run forever...
root.mainloop()
