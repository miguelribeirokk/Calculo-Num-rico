def simpson(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)

    for i in range(2, n-1, 2):
        integral += 2 * f(a + i * h)

    integral *= h / 3

    return integral

def exemplo_funcao(x):
    return x**2

a = 0
b = 1
n = 1000

# Exemplo de uso:
resultado_simpson = simpson(exemplo_funcao, a, b, n)
print(f"Resultado do método de Simpson: {resultado_simpson}")
