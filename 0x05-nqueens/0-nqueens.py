#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys

def is_valid(board, row, col):
    """
    Check if a queen can be placed at board[row][col]
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    def backtrack(row):
        if row == n:
            res = []
            for i in range(n):
                res.append([i, board[i]])
            print(res)
            return
        
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * n
    backtrack(0)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)

if __name__ == "__main__":
    main()
