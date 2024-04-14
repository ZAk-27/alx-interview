#!/usr/bin/python3
"""module.
"""
import sys


solutions = []
"""module.
"""
nm = 0
"""module.
"""
poz = None
"""module.
"""


def get_input():
    """module
    """
    global nm
    nm = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nm = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if nm < 4:
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
        if i == nm:
            return True
    return False


def build_solution(row, grp):
    """module.
    """
    global solutions
    global nm
    if row == nm:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * nm) + col
            matches = zip(list([poz[a]]) * len(grp), grp)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(poz[a].copy())
            if not any(used_positions):
                build_solution(row + 1, grp)
            group.pop(len(grp) - 1)


def get_solutions():
    """module.
    """
    global poz, nm
    poz = list(map(lambda x: [x // nm, x % n], range(nm ** 2)))
    a = 0
    grp = []
    build_solution(a, grp)


nm = get_input()
get_solutions()
for solution in solutions:
    print(solution)
