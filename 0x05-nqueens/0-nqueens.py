#!/usr/bin/python3
"""module.
"""
import sys


solutions = []
"""module.
"""
n = 0
"""module.
"""
poz = None
"""module.
"""


def get_input():
    """module
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(poz0, poz1):
    """module.
    """
    if (poz0[0] == poz1[0]) or (poz0[1] == poz1[1]):
        return True
    return abs(poz0[0] - poz1[0]) == abs(poz0[1] - poz1[1])


def group_exists(grp):
    """module.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_poz in stn:
            for grp_poz in grp:
                if stn_poz[0] == grp_poz[0] and stn_poz[1] == grp_poz[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, grp):
    """module.
    """
    global solutions
    global n
    if row == n:
        tmp0 = grp.copy()
        if not grp_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([poz[a]]) * len(grp), grp)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            grp.append(poz[a].copy())
            if not any(used_positions):
                build_solution(row + 1, grp)
            grp.pop(len(grp) - 1)


def get_solutions():
    """module.
    """
    global poz, n
    poz = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    grp = []
    build_solution(a, grp)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
