def funcao_exemplo(x):
    return x**2

def quadratura_gaussiana_2pontos(f, a, b):
    # Abscissas e pesos para 2 pontos
    x = [-1 / ((3)**0.5), 1 / ((3)**0.5)]
    w = [1, 1]

    # Mapeia as abscissas de [-1, 1] para [a, b]
    x_mapped = [(b - a) / 2 * xi + (a + b) / 2 for xi in x]

    # Calcula a soma ponderada da função nos pontos mapeados
    integral = sum(wi * f(xi) for wi, xi in zip(w, x_mapped))

    # Ajusta pela escala do intervalo [a, b]
    integral *= (b - a) / 2

    return integral

# Exemplo de uso
a = 0
b = 1

resultado_quadratura_gaussiana = quadratura_gaussiana_2pontos(funcao_exemplo, a, b)
print(f"Resultado da quadratura Gaussiana (2 pontos): {resultado_quadratura_gaussiana}")
