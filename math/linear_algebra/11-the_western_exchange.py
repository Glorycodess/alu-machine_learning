#!/usr/bin/env python3
"""
Function to return the transpose of a numpy.ndarray
"""

import numpy as np

def np_transpose(matrix):
    """Returns a new transposed numpy.ndarray of the input matrix"""
    return np.array(matrix).T
