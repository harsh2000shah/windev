# !/usr/bin/python3
# importing shits....
from tkinter import *
from tkinter import filedialog
import xlrd
import psycopg2
import sys
from elevate import elevate


# create a root object... like body in html
root = Tk()

# title just like the html thingie... and icon... near the title...
root.title("AaplaHR | Register")
icon_photo = PhotoImage(file="logistics64.png")
root.iconphoto(False, icon_photo)


# ****************************   VARIABLES ********************************

# ****************************   FUNCTIONS ********************************
def browse():
    filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select an Excel file",
                                          filetype=(("Excel Files", "*.xlsx"),))

    conn = psycopg2.connect(
        host="ec2-18-210-90-1.compute-1.amazonaws.com",
        database="d5vsj8ca6ts06",
        user="lvoyfxcjoqmbxa",
        password="d971190b2bd5645d023f5c93a1b78a5c701576f0009fa3d6903a12ce3770ce72",
        port=5432
    )
    print("Connected to DB successfully")
    cur = conn.cursor()

    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    numberOfRows = sheet.nrows

    for i in range(1, numberOfRows):
        dataList = []
        dataList = sheet.row_values(i)
        cur.execute(
            "INSERT INTO employees (firstName, lastName, empCode, bioCode) VALUES ('" + str(dataList[0]) + "', '" + str(
                dataList[1]) + "', '" + str(dataList[2]) + "', '" + str(dataList[3]) + "')")
    conn.commit()
    print("Records created successfully")
    conn.close()
    sys.exit()

# the company picture...
photo = PhotoImage(file="image.png")
label_photo = Label(root, image=photo, height=100, bg="#00BFFF").pack(fill="both", expand=True, ipady=20, ipadx=50)

canvas = Canvas(root, height=0, width=0, bd=0, bg="#00BFFF", highlightthickness=0)

var_text1 = "Please click Browse button to select an"
label = Label(canvas, text=var_text1, bg="#00BFFF", fg="white", font=('calibre', 12, 'bold'))
label.pack(fill="both", expand=True)
var_text2 = "Excel* file to upload"
label = Label(canvas, text=var_text2, bg="#00BFFF", fg="white", font=('calibre', 12, 'bold'))
label.pack(fill="both", expand=True)

browse_btn = Button(canvas, text="Browse", font=('normal', 12, 'bold'), fg="white", bg="forest green",
                    command=browse).pack(pady=(30, 30))

canvas.pack(fill="both", expand=True)

# run forever...
root.mainloop()
