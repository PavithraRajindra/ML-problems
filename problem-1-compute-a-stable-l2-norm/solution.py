import numpy as np


def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    x = np.asarray(x, dtype = float)
    scaling_factor = np.max(np.abs(x))
    if scaling_factor == 0:
        return 0.0
    return float(scaling_factor * np.sqrt(np.sum((x/scaling_factor)**2)))
