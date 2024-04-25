#!/usr/bin/python3
"""
matrix 2D a rotation module.
"""


def rotate_2d_matrix(matrix):
    """
    documentation documnts documntations.
    """
    i = 0
    for v in list(zip(*matrix)):
        matrix[i][:] = v[::-1]
        i += 1
