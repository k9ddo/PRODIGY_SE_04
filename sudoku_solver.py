import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[(row//3)*3+i//3][(col//3)*3+i%3] == num:
            return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def solve_gui():
    board = [[int(entries[r][c].get() or 0) for c in range(9)] for r in range(9)]
    if solve(board):
        for r in range(9):
            for c in range(9):
                entries[r][c].delete(0, tk.END)
                entries[r][c].insert(0, str(board[r][c]))
    else:
        messagebox.showerror("Sudoku", "No solution exists")

sudoku = tk.Tk()
sudoku.title("Sudoku Solver")

entries = [[tk.Entry(sudoku, width=2, font=('Arial', 18)) for _ in range(9)] for _ in range(9)]
for r in range(9):
    for c in range(9):
        entries[r][c].grid(row=r, column=c)

tk.Button(sudoku, text="Solve", command=solve_gui).grid(row=9, column=0, columnspan=9, pady=10)

sudoku.mainloop()
