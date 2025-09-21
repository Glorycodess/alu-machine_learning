#!/usr/bin/env python3
"""Module that calculates the minor matrix of a square matrix."""


def determinant(matrix):
    """Recursively calculate the determinant of a square matrix."""
    if matrix == [[]]:
        return 1
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sub = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub)
    return det


def minor(matrix):
    """Calculate the minor matrix of a square matrix.

    Args:
        matrix (list of lists): the input matrix

    Returns:
        list of lists: minor matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a non-empty square matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [] or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if n == 1:
        return [[1]]

    minors = []
    for i in range(n):
        row_minors = []
        for j in range(n):
            sub = [r[:j] + r[j + 1:] for k, r in enumerate(matrix) if k != i]
            row_minors.append(determinant(sub))
        minors.append(row_minors)
    return minors
