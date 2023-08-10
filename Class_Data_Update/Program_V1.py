"""
Author: 
Creed Jones

Summary: 
Take a text document and take the data then turn it into an excel sheet to save time
"""

import numpy
import openpyxl
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog


def program(input_file, output_path, class_code, school_code, semester):
    file = open(input_file, "r",  encoding="utf-8")
    content = file.readlines() #This is a list 

    content = [x.strip() for x in content]

    while("" in content):
        content.remove("")

    for x in content:
        x = x.replace("â€“", "999")

    endList = []
    for x in range(int(len(content) / 9)):
        temp = []
        for y in range(9):
            currentNum = (x * 9) + y
            if(y == 0):
                endList.append(temp)
                temp.clear()
                temp.append(semester + "-BL-" + school_code + "-" + class_code + "-" + content[(x * 9) + y])
            elif(y == 2 or y == 5):
                temp.append(content[(x * 9) + y])
            elif(y == 6):
                temp.insert(0, content[(x * 9) + y])
                temp.insert(0, ' ')
                temp.insert(1, ' ')
                temp.insert(3, ' ')
                temp.insert(4, ' ')
                temp.insert(5, ' ')
                temp.insert(6, ' ')
                temp.insert(7, ' ')
                temp.insert(8, ' ')
                temp.insert(9, ' ')
                temp.insert(11, ' ')

    arr = numpy.array(endList)
    df = pd.DataFrame(arr, columns = ['Course/Guide Name:', '', 'Instructor(s) or Contact:', '' , 'Instructor E-mail:', '', 'Guide URL:', '', 'Embedded In Canvas:', '', 'Metadata:', '', 'When:', 'Where:'])
    #df.to_excel('test.xlsx', sheet_name='Sheet 1')
    path = output_path + "/Results.xlsx"
    with pd.ExcelWriter(path) as writer:
        df.to_excel(writer, sheet_name = "Sheet 1")

app = tk.Tk()

btn_next = tk.Button(
    master = app,
    text = "Run",
    width = 25,
    height = 5,
    bg = "white",
    fg = "black"
)

class_code = Text(app, height = 3,
                width = 25,
                bg = "light yellow")

school_code = Text(app, height = 3,
                width = 25,
                bg = "light yellow")

semester = Text(app, height = 3,
                width = 25,
                bg = "light yellow")

def handle_click(event):
    USER_FILE = filedialog.askopenfilename()
    print(USER_FILE)
    USER_SAVE = filedialog.askdirectory()
    print(USER_SAVE)
    CLASS_CODE = class_code.get("1.0", "end-1c")
    SCHOOL_CODE = school_code.get("1.0", "end-1c")
    SEMESTER = semester.get("1.0", "end-1c")
    btn_next.destroy()
    class_code.destroy()
    school_code.destroy()
    semester.destroy()
    lbl_name2.destroy()
    lbl_name3.destroy()
    program(USER_FILE, USER_SAVE, CLASS_CODE, SCHOOL_CODE, SEMESTER)
    print("Done")
    lbl_name1.configure(text = "Done")


lbl_name1 = tk.Label(master = app, text = "Enter Class Code (Example C304)")
lbl_name2 = tk.Label(master = app, text = "Enter School Code (Example BUS)")
lbl_name3 = tk.Label(master = app, text = "Enter Semester (Example FA23)")

lbl_name1.pack()
class_code.pack()
lbl_name2.pack()
school_code.pack()
lbl_name3.pack()
semester.pack()
btn_next.pack()

btn_next.bind("<Button-1>", handle_click)
app.mainloop()