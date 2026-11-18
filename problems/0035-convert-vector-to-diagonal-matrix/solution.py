import numpy as np

def make_diagonal(x):
    mat = [[0.0 for _ in range(len(x))] for _ in range(len(x))]

    for i in range(len(x)):
        mat[i][i] = float(x[i])

    return mat
    