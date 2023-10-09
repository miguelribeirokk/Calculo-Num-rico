import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        L[i, i] = 1.0
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
    return L, U

def lu_solver(A, b):
    L, U = lu_decomposition(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x

# Exemplo de uso:
A = np.array([[2, 1, -1], [1, 3, 2], [3, 2, 4]], dtype=float)
b = np.array([8, 13, 22], dtype=float)
x = lu_solver(A, b)
print("Solução usando Decomposição LU:", x)
