"""
Author: 
Creed Jones

Summary: 
Take a text document and take the data then turn it into an excel sheet to save time
"""

import numpy
import pandas as pd
import openpyxl

CLASS_CODE = "C104"
SCHOOL_CODE = "BUS"
SEMESTER = "FA23"

input_path = "Projects-Learning\Class_Data_Update\Class_Data.txt"

file = open(input_path, "r",  encoding="utf-8")
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
            temp.append(SEMESTER + "-BL-" + SCHOOL_CODE + "-" + CLASS_CODE + "-" + content[(x * 9) + y])
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
            temp.insert(10, ' ')

arr = numpy.array(endList)
df = pd.DataFrame(arr, columns = ['Course/Guide Name:', '', 'Instructor(s) or Contact:', '' , 'Instructor E-mail:', '', 'Guide URL:', '', 'Embedded In Canvas:', '', 'Metadata:', '', 'When:', 'Where:'])
df.to_excel('test.xlsx', sheet_name='Sheet 1')