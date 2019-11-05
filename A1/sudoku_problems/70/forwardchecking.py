import numpy as np
import random
import sys

def used_in_row(grid,row,num):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False

def used_in_col(grid,col,num):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False

def used_in_box(grid,row,col,num):
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col] == num:
                return True
    return False

def safe_location(grid,row,col,num):
    return not used_in_row(grid,row,num) and not used_in_col(grid,col,num) and not used_in_box(grid,row -row%3,col - col%3,num)

def empty_squares(grid):
    empty_squares = []
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                empty_squares.append([row,col])
    return empty_squares

def random_square(empty_squares):
    return empty_squares[random.randint(0,len(empty_squares)-1)]

def find_available_domain(grid):
    domain = []
    [domain.append(list(range(1,10))) for i in range(81)]
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                value = grid[row][col]
                remove_domain(domain,value,row,col)
    return domain

def remove_domain(domain,value,row,col):
    for r in domain[row*9:row*9+9]:
        try:
            r.remove(value)
        except ValueError:
            pass
    
    for c in range(9):
        try:
            domain[col+9*c].remove(value)
        except ValueError:
            pass
        
    b_col = int(col / 3)
    b_row = int(row / 3)
    for i in range(3):
        for j in range(3):
            try:
                domain[b_col*3 + j + (b_row*3+i)*9].remove(value)
            except ValueError:
                pass

def forward_checking(domain,value,row,col):
    for i in range(9):
        x = domain[row*9+i]
        if len(x) == 1:
            if x[0] == value:
                return False
    for i in range(9):
        x = domain[col+9*i]
        if len(x) == 1:
            if x[0] == value:
                return False
    b_row = int(row / 3)
    b_col = int(col / 3)
    
    for i in range(3):
        for j in range(3):
            x = domain[b_col*3+j+(b_row*3+i)*9]
            if len(x) == 1:
                if x[0] == value:
                    return False
    return True

def sudoku_solver(grid):
    empty = empty_squares(grid)
    if len(empty) == 0:
        return True
    square = random_square(empty)
    row = square[0]
    col = square[1]
    
    available_domain = find_available_domain(grid)
    values = available_domain[col+row*9]
    
    while len(values) != 0:
        value = values[random.randint(0,len(values)-1)]
        values.remove(value)
        if forward_checking(available_domain,value,row,col):
            grid[row][col] = value
            if sudoku_solver(grid):
                return True
            grid[row][col] = 0
    return False

file = sys.argv[1]
matrix = np.loadtxt(file)
sudoku_solver(matrix)
print(matrix)
