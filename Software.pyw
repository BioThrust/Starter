import tkinter as tk
from tkinter import *
import webbrowser

root= tk.Tk()
root.title("Hello!")
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    link = Label(root, text="http://biothrust.herokuapp.com", fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))
    
button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()