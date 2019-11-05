import numpy as np
import random
import sys

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
                domain = remove_domain(domain,value,row,col)
    return domain

def remove_domain(domain,value,row,col):
    domain[col+row*9] = [0]
    for r in domain[row*9:row*9+9]:
        if r == 0:
            continue
        try:
            r.remove(value)
        except ValueError:
            pass
    
    for c in range(9):
        if domain[col+9*c] == 0:
            continue
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
            
    return domain
            
def forward_checking(domain,value,row,col):
    for i in range(9):
        if i == col:
            continue
        x = domain[row*9+i]
        if len(x) == 1:
            if x[0] == value:
                return False    
    
    for i in range(9):
        if i == row:
            continue
        x = domain[col+9*i]
        if len(x) == 1:
            if x[0] == value:
                return False
    
    b_row = int(row / 3)
    b_col = int(col / 3)
    
    for i in range(3):
        for j in range(3):
            if [b_row*3+i ,b_col*3+j] == [row,col]:
                continue
            x = domain[b_col*3+j+(b_row*3+i)*9]
            if len(x) == 1:
                if x[0] == value:
                    return False
    return True

def find_degree(square,grid):
    row = square[0]
    col = square[1]
    degree = 0
    
    for i in range(9):
        if i == col:
            continue
        if grid[i][col] == 0:
            degree += 1
    
    for i in range(9):
        if i == row:
            continue
        if grid[row][i] == 0:
            degree += 1
            
    b_col = int(col/3)
    b_row = int(row/3)
    
    for i in range(3):
        for j in range(3):
            if [b_row*3+i,b_col*3+j] == [row,col]:
                continue
            if grid[b_row*3+i][b_col*3+j] == 0:
                degree += 1
    return degree

def get_lcs(available_domain,values,row,col):
    lcs = []
    
    for i in values:
        neighbour = 0
        
        for j in range(9):
            if i == col:
                continue
            x = available_domain[row*9+j]
            if i in x:
                neighbour += 1
        
        for j in range(9):
            if j == row:
                continue
            x = available_domain[col+9*j]
            if i in x:
                neighbour += 1
        
        b_col = int(col/3)
        b_row = int(row/3)
        
        for j in range(3):
            for k in range(3):
                if [b_row*+j,b_col*3+k] == [row,col]:
                    continue
                x = available_domain[b_col*3+k+(b_row*3+j)*9]
                if i in x:
                    neighbour += 1
        lcs.append(neighbour)
    return lcs

def sudoku_solver(grid):
    mrv = []
    mrv_squares = []
    empty = empty_squares(grid)
    if len(empty) == 0:
        return True
    
    available_domain = find_available_domain(grid)
    
    [mrv.append(len(available_domain[cell[0]*9+cell[1]])) for cell in empty]
    
    min_mrv = min(mrv)
    
    for i in range(len(mrv)):
        if mrv[i] == min_mrv:
            mrv_squares.append(empty[i])
    
    if len(mrv_squares) == 1:
        square = mrv_squares[0]
    
    else:
        degree = []
        
        for square in mrv_squares:
            d = find_degree(square,grid)
            degree.append(d)
            
        maxdegree = max(degree)
        max_degree = []
        for i in range(len(degree)):
            if maxdegree == degree[i]:
                square = mrv_squares[i]
                
    row = square[0]
    col = square[1]
    
    values = available_domain[col+row*9]
    
    while len(values) != 0:
        lcs = get_lcs(available_domain,values,row,col)
        value = values[lcs.index(min(lcs))]
        values.remove(value)
        if forward_checking(available_domain,value,row,col):
            grid[row][col] = value
            if sudoku_solver(grid):
                return True
            else:
                grid[row][col] = 0
    return False

file = sys.argv[1]
matrix = np.loadtxt(file)
sudoku_solver(matrix)
print(matrix)