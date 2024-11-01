# sudoku_solver_gui.py

import tkinter as tk
from sudoku_solver import solve_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[0] * 9 for _ in range(9)]
        self.cells = [[None] * 9 for _ in range(9)]
        self.create_board()
        self.create_buttons()

    def create_board(self):
        """Create 9x9 grid for Sudoku board input."""
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=5, pady=5)
                self.cells[row][col] = entry

    def create_buttons(self):
        """Create Solve and Clear buttons."""
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=5, sticky="we")
        clear_button = tk.Button(self.root, text="Clear", command=self.clear)
        clear_button.grid(row=9, column=5, columnspan=5, sticky="we")

    def get_board(self):
        """Retrieve the current board state from the GUI."""
        for row in range(9):
            for col in range(9):
                val = self.cells[row][col].get()
                self.board[row][col] = int(val) if val.isdigit() else 0

    def display_board(self):
        """Display the solved board in the GUI."""
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(self.board[row][col]))

    def solve(self):
        """Solve the Sudoku puzzle and display the solution."""
        self.get_board()
        if solve_sudoku(self.board):
            self.display_board()
        else:
            tk.messagebox.showerror("Error", "No solution exists")

    def clear(self):
        """Clear the board."""
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.board[row][col] = 0

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
