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
        raise ValueError("N must be at least 4")
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
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: nqueens N")
    try:
        n = int(sys.argv[1])
    except ValueError:
        raise ValueError("N must be a number")
    print_solutions(n)
