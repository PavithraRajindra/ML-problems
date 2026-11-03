import numpy as np


def solve(X):
    # TODO: Return the Gram matrix X^T X.
    X = np.asarray(X, float)
    return X.T @ X
