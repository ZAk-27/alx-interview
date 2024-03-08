#!/usr/bin/python3
""" pascal trizngle func"""


def pascal_triangle(n):
    """Creates a list of lists of integers representing
    the Pascal's triangle of a given integer."""

    if n <= 0:
        return []
    tp = [[1]]
    for fn_number in range(1, n):
        fn = [1]
        for j in range(1, fn_number):
            element = tp[fn_number - 1][j - 1] + tp[fn_number - 1][j]
            fn.append(element)
        fn.append(1)
        tp.append(fn)

    return tp
