import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    x = np.asarray(x, dtype = float)
    x_norm = np.linalg.norm(x)
    if x_norm == 0:
            raise ValueError()
    return x/x_norm
