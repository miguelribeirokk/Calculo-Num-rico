def lagrange_interpolation(x, y, xi):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Exemplo de uso:
x = [0.1, 0.2, 0.4]
y = [2.82, 2.67, 2.43]
xi = 0.25
result = lagrange_interpolation(x, y, xi)
print(f"Interpolação de Lagrange em {xi} = {result}")