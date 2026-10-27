import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    if a_norm == 0 or b_norm == 0:
        return 0.0
    return float((a @ b) / (a_norm * b_norm)) # a@b is dot product
    # cos theta = (a dot_product b) / (norm_a * norm_b)
