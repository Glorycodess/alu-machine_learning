#!/usr/bin/env python3
"""
Perform element-wise arithmetic operations on two arrays
"""

import numpy as np

def np_elementwise(mat1, mat2):
    """
    Returns a tuple containing element-wise addition, subtraction,
    multiplication, and division of mat1 and mat2
    """
    a = np.array(mat1)
    b = np.array(mat2)
    return (a + b, a - b, a * b, a / b)
