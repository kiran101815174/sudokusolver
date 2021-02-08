#Set-ExecutionPolicy Unrestricted -Scope Process
#set FLASK_APP=routes.py
#set FLASK_APP=app.py

import flask
from flask import render_template,request
from flask import Flask


app=Flask(__name__,static_url_path='/static')

def find_emp_locations(arr,l):
    for j in range(9):
        for i in range(9):
            if arr[j][i]==0:
                l[0]=j
                l[1]=i
                return True
    return False
def checkbox(arr,row,col,num):
    #check for row
    for i in range(9):
        if arr[row][i]==num:
            return False
    #check for column
    for j in range(9):
        if arr[j][col]==num:
            return False
    #check for subgrid
    row_box=row-row%3
    col_box=col-col%3
    for i in range(3):
        for j in range(3):
            if(arr[row_box+i][col_box+j]==num):
                return False
    return True
def solvesudoku(arr):
    l=[0,0]
    if(not find_emp_locations(arr,l)):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,10):
        if(checkbox(arr,row,col,num)):
            arr[row][col]=num
            if(solvesudoku(arr)):
                return True
        arr[row][col]=0
    return False



            
        
        
    
@app.route('/')
def main():
    puzzle = [['' for i in range(9)] for i in range(9)]
    return render_template('sudoku.html',puzzle=puzzle, message="Solve Puzzle")


@app.route('/results',methods=['POST'])
def displaysolution():
    cells=request.form.getlist("cells[]",type=int)
    if 0 in cells:
        puzzle=[]
        for i in range(9):
            puzzle.append(cells[i*9:(i+1)*9])
        solvesudoku(puzzle)
        return render_template('sudoku.html', puzzle=puzzle,message="resetBoard")
    else:
        puzzle = [['' for i in range(9)] for i in range(9)]
        return render_template("sudoku.html", puzzle=puzzle, message="Solve Puzzle")