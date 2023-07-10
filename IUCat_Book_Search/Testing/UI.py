import tkinter as tk
from tkinter import filedialog

start = tk.Tk()
lbl_name = tk.Label(text="IUCAT search")
lbl_name.pack()

btn_next = tk.Button(
    text = "Run",
    width = 25,
    height = 5,
    bg = "white",
    fg = "black"
)


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

#btn_next.pack()

def handle_click(event):
    print("The button was clicked!")
    #TODO Track what number we are on and pull up the next number
    #This might not work because the fuction will run and end  
    if(screen == 0):
        getFile()
    elif(screen == 1):
        progressScreen()
    else:
        endScreen()
    screen += 1

def endScreen():
    print("Here is the file")
    #TODO Return the file to the user (AKA where to save?)

def progressScreen():
    print("Screen 3")
    #TODO Run the program with the given file

def getFile():
    print("Screen 2")
    #TODO Get file from user and get ready to send to program

def startScreen():
    #TODO Instructions
    lbl_name.pack()
    btn_next.pack()
    btn_next.bind("<Button-1>", handle_click)
    start.mainloop()
    #TODO Close

startScreen()

#I might need this later
#https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/