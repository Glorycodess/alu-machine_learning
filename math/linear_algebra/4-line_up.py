#!/usr/bin/env python3
"""
Add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Parameters:
        arr1 (list of int/float): first array
        arr2 (list of int/float): second array

    Returns:
        list: element-wise sum of arr1 and arr2
        None: if arrays are not the same shape
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
