#     ****************************** SUCCESSFULL ***********************************************************
# from tkinter import *
# from tkinter import filedialog
# import xlrd
# import psycopg2
#
# filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select an Excel file",
#                                       filetype=(("Excel Files", "*.xlsx"),))
#
# conn = psycopg2.connect(
#     host="ec2-18-210-90-1.compute-1.amazonaws.com",
#     database="d5vsj8ca6ts06",
#     user="lvoyfxcjoqmbxa",
#     password="d971190b2bd5645d023f5c93a1b78a5c701576f0009fa3d6903a12ce3770ce72",
#     port=5432
# )
# print("Connected to DB successfully")
# cur = conn.cursor()
#
# wb = xlrd.open_workbook(filename)
# sheet = wb.sheet_by_index(0)
# sheet.cell_value(0, 0)
# numberOfRows = sheet.nrows
#
# for i in range(1, numberOfRows):
#     dataList = []
#     dataList = sheet.row_values(i)
#     cur.execute("INSERT INTO employees (firstName, lastName, empCode, bioCode) VALUES ('" + str(dataList[0]) + "', '" + str(dataList[1]) + "', '" + str(dataList[2]) + "', '" + str(dataList[3]) + "')")
#
# conn.commit()
# print("Records created successfully")
# conn.close()

#     ****************************** NOT SUCCESS FULL DUE TO LOGS IN DIFFERENT LINES IN DB *****************
# from tkinter import *
# from tkinter import filedialog
# import xlrd
# import psycopg2
#
# filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select an Excel file",
#                                       filetype=(("Excel Files", "*.xlsx"),))
#
# conn = psycopg2.connect(
#     host="ec2-18-210-90-1.compute-1.amazonaws.com",
#     database="d5vsj8ca6ts06",
#     user="lvoyfxcjoqmbxa",
#     password="d971190b2bd5645d023f5c93a1b78a5c701576f0009fa3d6903a12ce3770ce72",
#     port=5432
# )
# print("Connected to DB successfully")
# cur = conn.cursor()
#
# wb = xlrd.open_workbook(filename)
# sheet = wb.sheet_by_index(0)
# sheet.cell_value(0, 0)
# numberOfRows = sheet.nrows
# print(numberOfRows)
# i = 1     # the number of rows starts from 0 for the first row...
# dataList = []
#
# for j in range(numberOfRows):
#     dataList.append([])
#     for n in range(4):
#         dataList[j].append("o")
#
# for k in range(1, numberOfRows - 1):
#     for m in range(0, 3):
#         variable_entry = sheet.cell_value(k, m)
#         variable_entry = str(variable_entry)
#         if m == 0:
#             cur.execute("INSERT INTO employees (firstName) VALUES ('" + variable_entry + "');")
#         elif m == 1:
#             cur.execute("INSERT INTO employees (lastName) VALUES ('" + variable_entry + "');")
#         elif m == 2:
#             cur.execute("INSERT INTO employees (empCode) VALUES ('" + variable_entry + "');")
#         elif m == 3:
#             cur.execute("INSERT INTO employees (bioCode) VALUES (" + variable_entry + ");")
#         else:
#             print("Unexpected data")
#
# print(dataList)
# conn.commit()
# print("Records created successfully")
# conn.close()
