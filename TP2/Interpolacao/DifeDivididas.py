def divided_differences(x, y):
    n = len(x)
    f = [[0] * n for _ in range(n)]
    
    for i in range(n):
        f[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])
    
    return f[0]

def newton_interpolation(x, y, xi):
    n = len(x)
    result = 0.0
    coefficients = divided_differences(x, y)
    
    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (xi - x[j])
        result += term
    
    return result

# Exemplo de uso:
x = [0.1, 0.2, 0.4]
y = [2.82, 2.67, 2.43]
xi = 0.25
result = newton_interpolation(x, y, xi)
print(f"Interpolação de Newton em {xi} = {result}")