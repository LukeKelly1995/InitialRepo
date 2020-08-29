"""This is a test main file
"""
import numpy as np


def zeros_function(a, b):
    """This is a sample function

	Args:
		a (int): any integer
		b (int): any integer
	"""
    array = np.zeros((a, b))
    print(array)


if __name__ == "__main__":
    """This is test main function
	"""
    zeros_function(2, 2)
