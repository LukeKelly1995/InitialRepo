"""This is a module for numpy utils."""

import numpy as np


def zeros_function(a, b):
    """This is a sample function

	Args:
		a (int): any integer
		b (int): any integer
	"""
    array = np.zeros((a, b))
    print(array)
