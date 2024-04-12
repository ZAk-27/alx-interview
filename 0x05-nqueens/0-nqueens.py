#!/usr/bin/python3
"""N queens solution finder module"""
import sys


def solve_queens_problem(board_size):
    """N queens solution finder module"""

    def is_valid_position(plc, occupied_plc):
        """N queens solution finder module"""
        for i in range(len(occupied_plc)):
            if (
                occupied_plc[i] == plc or
                occupied_plc[i] - i == plc - len(occupied_plc) or
                occupied_plc[i] + i == plc + len(occupied_plc)
            ):
                return False
        return True

    def place_queens(board_size, index, occupied_plc, solutions):
""" N queens solution finder module"""
        if index == board_size:
            solutions.append(occupied_plc[:])
            return

        for i in range(board_size):
            if is_valid_position(i, occupied_plc):
                occupied_plc.append(i)
                place_queens(board_size, index + 1, occupied_plc, solutions)
                occupied_plc.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """N queens solution finder module"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()
