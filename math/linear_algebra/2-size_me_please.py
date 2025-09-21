#!/usr/bin/env python3
"""Module to calculate the shape of a matrix."""

def matrix_shape(matrix):
    """
    Calculates the shape of a matrix (nested list).

    Args:
        matrix (list): A nested list representing the matrix.

    Returns:
        list: A list of integers representing the size of each dimension.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
