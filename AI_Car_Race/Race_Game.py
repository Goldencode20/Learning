"""
Author: Creed Jones

Summary:

Next Steps: 
    Get image files working 
    Place image on screen
"""

import tkinter
from tkinter import * 

# Set up screen
screen = tkinter.Tk()
screen.title('Race Game')
screen.geometry("500x500")

# Do this when key is pressed
def key_press(e):
   #label.config(text="Hello World!")
   label.config(text = e.keysym) # Return the key pressed

# Create a label widget to add some text
label= Label(screen, text = "", font = ('Helvetica 17 bold'))
label.pack(pady = 50)

# Bind the key press and run when key is pressed
screen.bind('<KeyPress>', key_press)
screen.mainloop()