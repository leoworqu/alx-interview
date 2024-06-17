#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list): The matrix to rotate.

    Returns:
        list of list: The rotated matrix.
    """

    n = len(matrix)

    def transpose_matrix():
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse_matrix():
        for row in matrix:
            row.reverse()

    transpose_matrix()
    reverse_matrix()

    return matrix
