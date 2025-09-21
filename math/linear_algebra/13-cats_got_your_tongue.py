#!/usr/bin/env python3
"""Module to concatenate two numpy arrays along a specified axis."""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenate two numpy arrays along a given axis.

    Args:
        mat1 (numpy.ndarray): First array.
        mat2 (numpy.ndarray): Second array.
        axis (int): Axis along which to concatenate (0 or 1).

    Returns:
        numpy.ndarray: Concatenated array.
    """
    return np.concatenate((mat1, mat2), axis=axis)
