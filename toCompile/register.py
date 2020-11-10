# !/usr/bin/python3
# importing shits....
from tkinter import *
from tkinter import filedialog
import xlrd
import psycopg2
import sys
from elevate import elevate
import os as os
import ctypes

# used to get admin permission...
# elevate()

# create a root object... like body in html
root = Tk()

# title just like the html thingie... and icon... near the title...
root.title("AaplaHR | Register")
icon_photo = PhotoImage(file="logistics64.png")
root.iconphoto(False, icon_photo)

# ****************************   VARIABLES ********************************
# declaring string variables... ID and password
id_var = StringVar()
pass_var = StringVar()


# ****************************   FUNCTIONS ********************************
# defining a function that will get the id and password and then will print on the screen...
def submit():
    id_ = id_var.get()
    password = pass_var.get()
    conn = psycopg2.connect(
        host="ec2-52-71-153-228.compute-1.amazonaws.com",
        database="d3bqo8sugrakjr",
        user="xhmwyzyzdjapsv",
        password="0b0d9e0c6cb8e80f6d895b870a8ad709e81e478ef271c67869ac643cf4fe17ae",
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT password FROM CLIENTS_LOGIN where id_='" + id_ + "';")

    rows = cur.fetchall()

    if len(rows) == 0:
        ctypes.windll.user32.MessageBoxW(0, "Username 404 (Not Found)", "Invalid Response", 1)

    for row in rows:
        password_got = str(row[0])
        conn.commit()
        conn.close()

        if password_got == password:
            id_var.set("")
            pass_var.set("")
            os.system('compile/phasetwo.exe')
            sys.exit()
        else:
            ctypes.windll.user32.MessageBoxW(0, "Entered Password is incorrect", "Invalid Response", 1)


# the company logo...
photo = PhotoImage(file="image.png")
label = Label(root, image=photo, height=100, bg="#00BFFF").pack(fill="both", expand=True, ipady=20, ipadx=50)

canvas = Canvas(root, height=300, width=500, highlightthickness=0, bg="#00BFFF")
# ******************************************************************************************************
# creating label for input...
id_label = Label(canvas, text="Enter ID                                ", font=('calibre', 14, 'bold'), fg="white",
                 bg="#00BFFF").pack()
id_entry = Entry(canvas, textvariable=id_var, font=('calibre', 12, 'normal'), bg="white", bd=5, width=25).pack(
    ipady=2)

# creating label for input...
pass_label = Label(canvas, text="Password                             ", font=('calibre', 14, 'bold'), fg="white",
                   bg="#00BFFF").pack(pady=(20, 0))
pass_entry = Entry(canvas, textvariable=pass_var, font=('calibre', 12, 'normal'), bg="white", width=25, bd=5,
                   show="*").pack(ipady=2)

# creating the sub button...
sub_btn = Button(canvas, text='Submit', font=('normal', 12, 'bold'), fg="white", bg="forest green",
                 command=submit).pack(pady=(30, 30))

# ******************************************************************************************************
canvas.pack(fill="both", expand=True)

# run forever!
root.mainloop()
