import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def popup():
    popup_window = tk.Toplevel()
    popup_window.title("popup")
    popup_window.config(width=300, height=200)
    button_close = ttk.Button(popup_window, text="close", command=popup_window.destroy)
    button_close.place(x=75,y=75)


root = tk.Tk()
root.config(width=400, height=300)
root.title("Main Window")
button_open = ttk.Button(root, text="popup", command=popup)
button_open.place(x=100,y=100)


def on_drag_start(event):
    event.widget._start_x = event.x
    event.widget._start_y = event.y

def on_drag(event):
    w = event.widget
    x = w.winfo_x() - w._start_x + event.x
    y = w.winfo_y() - w._start_y + event.y
    w.place(x=x,y=y)

label = ttk.Label(root, text="")
bigimage = Image.open("randomimage.png")
img2 = bigimage.resize((75,75))
img = ImageTk.PhotoImage(image=img2)
label['image'] = img
label.bind("<Button-1>", on_drag_start)
label.bind("<B1-Motion>", on_drag)
label.place(x=120, y=120)

root.mainloop()

"def checkValid "