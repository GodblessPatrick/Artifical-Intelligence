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

'''
def random_square(empty_squares):
    return empty_squares[
'''    
    

#def bk_solver(grid):

file = sys.argv[1]
matrix = np.loadtxt(file)
print(empty_squares(matrix))    