#!/usr/bin/env python3
"""A function that sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of the floats in the list"""
    return 0 if input_list is None else sum(input_list)
