import numpy as np
import sys

grid = [[0 for x in range(9)] for y in range(9)]
def input():
    file = sys.argv[1]
    data = open(file,"r")
    for line in data:
        a,b,c,d,e,f,g,h,i,j = line.spilt()
    data.close()


def empty_location(grid,l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

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

def sudoku_solver(grid):
    l = [0,0]
    if (not empty_location(grid,l)):
        return true
    row = l[0]
    col = l[1]
    for square in range(1,10):
        if safe_location(grid,row,col,num):
            grid[row][col] = num
            if sudoku_solver(grid):
                return True
            grid[row][col] = 0
            
    return False