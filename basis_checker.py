import numpy as np
import math
from collections import Counter
import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title("Basis Checker")

C = tk.Canvas(root, bg="white",height = 600, width = 1000)
C.grid(row=0, column=0)

# to get entires to appear on the side of the grid
sidebar = tk.Frame(root, padx=10, pady=10)
sidebar.grid(row=0, column=1, sticky="n")

# variables for storing n amd m values 
n_var = tk.IntVar() # number of columns
m_var = tk.IntVar() # number of rows
x_offset = 0
y_offset = 0
CELL_SIZE = 80
dim = 0     # dimension = number of tokens that can be placed

# Calculate the dimension, the number of tokens we can place 
# for all n >= m >= 1
def get_dim(m, n):
    global dim
    if m <= n and n <= (2*m - 1):
        dim = math.floor(2/3*(n + m - 1))
    else:
        dim = n - 1


# Get the dimensions of the grid and draw it 
def submit():
    global matrix, tokens
    C.delete("all")
    m = m_var.get()
    n = n_var.get()
    tokens = [] # initialize token array that stores coordinates of each token
    matrix = np.zeros((m, n), dtype=int) # initialize empty matrix
    print(matrix)
    get_dim(m, n)
    draw_grid(m_var.get(), n_var.get())

# Validates if the tokens placed are a metric basis or not
# m, n >= 2 
# (a) there is at most one empty row and at most one empty column
# (b) there is at most one lonely vertex, and
# (c) if there is an empty row and an empty column, then there is no lonely vertex.
def validate_basis():
    print("CHECKING BASIS")
    empty_cols = 0
    empty_rows = 0
    lonely_vert = 0

    # count number of lonely vertices
    x_counts = Counter(x for x, y in tokens)
    y_counts = Counter(y for x, y in tokens)
    lonely_vert = sum(1 for x, y in tokens if x_counts[x] == 1 and y_counts[y] == 1)

    # count number of empty cols and rows
    for col in range(len(matrix[0])):  
        if (matrix[:, col] == 0).all():
            empty_cols += 1
    for row in range (len(matrix)):
        if (matrix[row, :] == 0).all():
            empty_rows += 1
    
    #check lonley vertex
    xFreq = {}
    yFreq = {}
    for x,y in tokens:
        xFreq[x] = xFreq.get(x,0) +1
        yFreq[y] = yFreq.get(y,0)+1
    
    for x,y in tokens:
        if xFreq[x] ==1 and yFreq[y] == 1:
            lonely_vert+=1
    #print(xFreq,yFreq)
    #print(lonely_vert)
    if empty_cols > 1 or empty_rows > 1 or (empty_cols == 1 and empty_rows ==1 and lonely_vert >0) or lonely_vert >1:
        print("NOT VALID")
        return 
    else:
        print("VALID")
# Draw the n x m grid by displaying rectangles
def draw_grid(m, n):
    global  x_offset, y_offset
    C.update()
    x_offset = (C.winfo_width() - n * CELL_SIZE) // 2
    y_offset = (C.winfo_height() - m * CELL_SIZE) // 2

    for row in range(n):
        for col in range(m):
            x1 = x_offset + CELL_SIZE * row
            y1 = y_offset + CELL_SIZE * col
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            rectangle = C.create_rectangle(x1, y1, x2, y2, fill="white", outline="grey")

# Gets the coordinates for which cell to place a specified token when clicked
def get_cell(event):
    col = (event.x - x_offset) //CELL_SIZE
    col = min(col, n_var.get()- 1)
    row = (event.y - y_offset) //CELL_SIZE
    row = min(row, m_var.get() - 1)

    if 0 <= col < n_var.get() and 0 <= row < m_var.get():
        place_token(row, col)

# places a token in the specified row and col 
def place_token(row, col):
    if (row, col) in tokens: # check that the same cell isn't clicked again
        return
    
    if len(tokens) >= dim :    # maximum num of tokens has been placed
        return
    
    cell_x = x_offset + col * CELL_SIZE + CELL_SIZE //2
    cell_y = y_offset + row * CELL_SIZE + CELL_SIZE //2
    r = CELL_SIZE //3

    C.create_oval(cell_x - r, cell_y - r, cell_x + r, cell_y + r, fill="light blue" )
    tokens.append((row, col))
    matrix[row][col] = 1

# get n and m entries on sidebar
n_label = tk.Label(sidebar, text = "n (columns, must be >= m): ").grid(row=0, column=0)
n_entry = tk.Entry(sidebar, textvariable = n_var, width = 5).grid(row=0, column=1, sticky="w")

m_label = tk.Label(sidebar, text = "m (rows, must be >= 1): ").grid(row=1, column=0)
m_entry = tk.Entry(sidebar, textvariable = m_var, width = 5).grid(row=1, column=1, sticky="w")

sub_btn=tk.Button(sidebar, text = 'Submit', command = submit).grid(row=2, column=0, columnspan=2, pady=10)
C.bind("<Button-1>", get_cell)

global matrix 
valid_btn = tk.Button(sidebar, text = 'Validate Basis', command = lambda: validate_basis(matrix, tokens)).grid(row=3, column=0, columnspan=2, pady=10)
root.mainloop()