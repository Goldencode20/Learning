"""
Author: Creed Jones

Summary:

Next Steps: 
    Get image files working 
    Place image on screen
"""

import tkinter
from tkinter import * 

class Car:
    def __init__(self, master = None):
        self.master = master
        
        self.x = 0
        self.y = 0
        self.MAX_SPEED = 20
 
        # canvas object to create shape
        self.canvas = Canvas(master)
        self.body = self.canvas.create_rectangle(5, 5, 25, 25, fill = "black")
        self.canvas.pack()
 
        # calling class's movement method to
        # move the rectangle
        self.movement()

    def movement(self):
 
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        self.canvas.move(self.body, self.x, self.y)
 
        self.canvas.after(100, self.movement)

    # for motion in negative x direction
    def leftPress(self, event):
        if (self.x > -self.MAX_SPEED):
            self.x -= 5

    # for motion in positive x direction
    def rightPress(self, event):
        if (self.x < self.MAX_SPEED):
            self.x += 5
    # for motion in positive y direction
    def upPress(self, event):
        if (self.y > -self.MAX_SPEED):
            self.y -= 5
     
    # for motion in negative y direction
    def downPress(self, event):
        if (self.y < self.MAX_SPEED):
            self.y += 5
    """
    def leftRelease(self, event):
        self.x += 5 

    def rightRelease(self, event):
        self.x -= 5
    """
    def UpRelease(self, event):
        if(self.y < 0):
            self.y += 1
            self.UpRelease(event)

    def DownRelease(self, event):
        if(self.y > 0):
            self.y -= 1
            self.DownRelease(event)
    
    def LeftRelease(self, event):
        if(self.x < 0):
            self.x -= 1
            self.LeftRelease(event)

    def RightRelease(self, event):
        if(self.x > 0):
            self.x -= 1
            self.RightRelease(event)


master = Tk()
car = Car(master)

# This will bind arrow keys to the tkinter
# toplevel which will navigate the image or drawing
master.bind("<KeyPress-Left>", lambda e: car.leftPress(e))
master.bind("<KeyPress-Right>", lambda e: car.rightPress(e))
master.bind("<KeyPress-Up>", lambda e: car.upPress(e))
master.bind("<KeyPress-Down>", lambda e: car.downPress(e))
master.bind("<KeyRelease-Left>", lambda e: car.LeftRelease(e))
master.bind("<KeyRelease-Right>", lambda e: car.RightRelease(e))
master.bind("<KeyRelease-Up>", lambda e: car.UpRelease(e))
master.bind("<KeyRelease-Down>", lambda e: car.DownRelease(e))
     
# Infinite loop breaks only by interrupt
mainloop()