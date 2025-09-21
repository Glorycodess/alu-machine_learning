#!/usr/bin/env python3
"""Module that calculates the adjugate of a square matrix."""


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


def cofactor(matrix):
    """Return the cofactor matrix of a square matrix."""
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [] or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if n == 1:
        return [[1]]

    cof = []
    for i in range(n):
        row_cof = []
        for j in range(n):
            sub = [r[:j] + r[j + 1:] for k, r in enumerate(matrix) if k != i]
            val = determinant(sub)
            row_cof.append(((-1) ** (i + j)) * val)
        cof.append(row_cof)
    return cof


def adjugate(matrix):
    """Return the adjugate (adjoint) of a square matrix.

    Args:
        matrix (list of lists): input matrix

    Returns:
        list of lists: adjugate matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a non-empty square matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [] or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Cofactor then transpose
    cof = cofactor(matrix)
    n = len(cof)
    adj = [[cof[j][i] for j in range(n)] for i in range(n)]
    return adj
