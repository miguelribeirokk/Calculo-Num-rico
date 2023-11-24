def ponto_medio(f, a, b, n):
    h = (b - a) / n
    integral = 0

    for i in range(n):
        x_i = a + (i + 0.5) * h
        integral += h * f(x_i)

    return integral

# Exemplo de uso:
def exemplo_funcao(x):
    return x**2

a = 0
b = 1
n = 1000

resultado = ponto_medio(exemplo_funcao, a, b, n)
print(f"Resultado do método do ponto médio: {resultado}")
