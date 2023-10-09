import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        pivot_row = np.argmax(np.abs(A[i:, i])) + i
        A[[i, pivot_row]] = A[[pivot_row, i]]
        b[i], b[pivot_row] = b[pivot_row], b[i]
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

# Exemplo de uso:
A = np.array([[2, 1, -1], [1, 3, 2], [3, 2, 4]], dtype=float)
b = np.array([8, 13, 22], dtype=float)
x = gauss_elimination(A, b)
print("Solução usando Eliminação de Gauss:", x)
