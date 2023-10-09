def linear_interpolation(x, y, xi):
    n = len(x)
    for i in range(n - 1):
        if x[i] <= xi <= x[i + 1]:
            slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
            result = y[i] + slope * (xi - x[i])
            return result

# Exemplo de uso:
x = [0.1, 0.2, 0.4]
y = [2.82, 2.67, 2.43]
xi = 0.25
result = linear_interpolation(x, y, xi)
print(f"Interpolação Linear em {xi} = {result}")
