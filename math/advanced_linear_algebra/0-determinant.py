#!/usr/bin/env python3
"""Module to calculate the determinant of a square matrix."""


def determinant(matrix):
    """Calculate the determinant of a square matrix.

    Args:
        matrix (list of lists): The square matrix.

    Returns:
        float or int: Determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square.
    """
    # Validate input type
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Handle 0x0 matrix
    if matrix == [[]]:
        return 1

    n = len(matrix)

    # Check if matrix is square
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Recursive case: NxN matrix
    det = 0
    for col in range(n):
        # Build submatrix excluding first row and current column
        submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)
    return det
