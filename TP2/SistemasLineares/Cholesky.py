import numpy as np

def cholesky_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i, i] = np.sqrt(A[i, i] - np.sum(L[i, :i]**2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    return L

def cholesky_solver(A, b):
    L = cholesky_decomposition(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(L.T, y)
    return x

# Exemplo de uso:
A = np.array([[4, 6, 10], [6, 25, 19], [10, 19, 74]], dtype=float)
b = np.array([20, 67, 225], dtype=float)
x = cholesky_solver(A, b)
print("Solução usando Decomposição de Cholesky:", x)
