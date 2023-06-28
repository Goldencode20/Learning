import tkinter as tk
from tkinter import filedialog

app = tk.Tk()

btn_next = tk.Button(
    master = app,
    text = "Run",
    width = 25,
    height = 5,
    bg = "white",
    fg = "black"
)

def handle_click(event):
    USER_FILE = filedialog.askopenfilename()
    print(USER_FILE)
    USER_SAVE = filedialog.askdirectory()
    print(USER_SAVE)
    app.destroy()
    
    loading = tk.Tk()
    label = tk.Label(text="This is New Label text", font=('Helvetica 14 bold'))
    label.pack(pady= 30)
    #TODO When the program runs and does another loop run this line
    #label.configure(text = x + "/" + searchLines)
    loading.mainloop()

lbl_name = tk.Label(master = app, text = "IUCAT search \n Hello World")
lbl_name.pack()
btn_next.pack()
btn_next.bind("<Button-1>", handle_click)

app.mainloop()