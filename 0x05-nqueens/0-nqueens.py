#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(n):
    if n < 4:
        print("N must be at least 4")
        print()
        sys.exit(1)
    board = [[0] * n for _ in range(n)]
    solutions = []

    def solve_util(row):
        if row == n:
            solutions.append([list(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_util(row + 1)
                board[row][col] = 0

    solve_util(0)
    return solutions


def print_solutions(n):
    solutions = solve_n_queens(n)
    for solution in solutions:
        queen_positions = []
        for row_idx, row in enumerate(solution):
            for col_idx, cell in enumerate(row):
                if cell == 1:
                    queen_positions.append([row_idx, col_idx])
        print(queen_positions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        print()
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        print()
        sys.exit(1)
    print_solutions(n)
