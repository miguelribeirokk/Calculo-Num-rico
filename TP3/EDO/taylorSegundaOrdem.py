def taylor_segunda_ordem(f, f_prime, y0, t0, tn, h):
    # f: função que define a EDO (dy/dt = f(t, y))
    # f_prime: derivada parcial de f em relação a y (df/dy)
    # y0: condição inicial
    # t0: tempo inicial
    # tn: tempo final
    # h: tamanho do passo

    t = t0
    y = y0

    while t < tn:
        y += h * f(t, y) + 0.5 * h**2 * f_prime(t, y)
        t += h

    return y


t0 = 0
tn = 2
y0 = 0.5
h = 0.2

# Exemplo de uso:
def exemplo_edo(t, y):
    return y - t**2 + 1  # Exemplo de EDO: dy/dt = y - t^2 + 1

def exemplo_derivada(t, y):
    return 1  # Derivada parcial de f em relação a y (df/dy)



resultado_taylor_segunda_ordem = taylor_segunda_ordem(exemplo_edo, exemplo_derivada, y0, t0, tn, h)
print(f"Resultado do método de Taylor de segunda ordem: {resultado_taylor_segunda_ordem}")
