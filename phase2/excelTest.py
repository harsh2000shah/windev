import xlrd
from tkinter import *
from tkinter import filedialog

# assume the file name of the user selected excel file is in the 'filename' variable...

filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select an Excel file",
                                          filetype=(("Excel Files", "*.xlsx"),))

wb = xlrd.open_workbook(filename)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)
numberOfRows = sheet.nrows
i = 1
dataList = []

for j in range(numberOfRows):
    dataList.append([])
    for n in range(5):
        dataList[j].append("o")

while i < numberOfRows:
    dataList[i] = sheet.row_values(i)
    i += 1

print(dataList)
