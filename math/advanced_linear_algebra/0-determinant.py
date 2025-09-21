#!/usr/bin/env python3
"""
0-determinant.py
Module that calculates the determinant of a matrix.
"""


def determinant(matrix):
    """Calculates the determinant of a square matrix."""
    # Type check
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Empty matrix or [[]] is considered 0x0
    if matrix == [[]]:
        return 1

    n = len(matrix)
    # Square check
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive calculation
    det = 0
    for col in range(n):
        # Build submatrix excluding first row and current column
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)
    return det
