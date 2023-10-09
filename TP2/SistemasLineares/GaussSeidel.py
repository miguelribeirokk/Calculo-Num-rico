import numpy as np

def gauss_seidel(A, b, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n)
    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    raise Exception("O método de Gauss-Seidel não convergiu")

# Exemplo de uso:
A = np.array([[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]], dtype=float)
b = np.array([1, 1, 1, 1], dtype=float)
x = gauss_seidel(A, b)
print("Solução usando Gauss-Seidel:", x)