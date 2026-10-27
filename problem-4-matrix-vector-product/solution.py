import numpy as np


def solve(A, x):
    """Implement Matrix-Vector Product from the mathematical contract in README.md."""
    A = np.asarray(A, dtype = float)
    x = np.asarray(x, dtype = float)

    return np.array([row @ x for row in A])
    # row @ x does dot product of one row of a matrix with with vector x
