import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title("Basis Checker")

C = tk.Canvas(root, bg="white", height = 300, width = 400)
C.pack(expand=False)

n = 3
m = 4

# variables for storing n amd m values 
n_var = tk.IntVar()
m_var = tk.IntVar()
CELL_SIZE = 40

# Get the dimensions of the grid and draw it 
def submit():
    draw_grid(m_var.get(), n_var.get())

# Draw the n x m grid by displaying rectangles
def draw_grid(m, n):
    for row in range(m):
        for col in range(n):
            x1 = CELL_SIZE * row
            y1 = CELL_SIZE * col
            x2 = CELL_SIZE * (row + 1)
            y2 = CELL_SIZE * (col + 1)
            rectangle = C.create_rectangle(x1, y1, x2, y2, fill="white", outline="grey")



n_label = tk.Label(root, text = "n: ")
n_entry = tk.Entry(root, textvariable = n_var)
n_label.pack()
n_entry.pack()

m_label = tk.Label(root, text = "m: ")
m_entry = tk.Entry(root, textvariable = m_var)
m_label.pack()
m_entry.pack()

sub_btn=tk.Button(root, text = 'Submit', command = submit)
sub_btn.pack()


root.mainloop()