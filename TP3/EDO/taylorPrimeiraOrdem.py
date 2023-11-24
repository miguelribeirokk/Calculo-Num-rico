def taylor_primeira_ordem(f, y0, t0, tn, h):
    # f: função que define a EDO (dy/dt = f(t, y))
    # y0: condição inicial
    # t0: tempo inicial
    # tn: tempo final
    # h: tamanho do passo

    t = t0
    y = y0

    while t < tn:
        y += h * f(t, y)
        t += h

    return y

# Exemplo de uso:
def exemplo_edo(t, y):
    return y - t**2 + 1  # Exemplo de EDO: dy/dt = y - t^2 + 1

t0 = 0
tn = 2
y0 = 0.5
h = 0.2

resultado_taylor_primeira_ordem = taylor_primeira_ordem(exemplo_edo, y0, t0, tn, h)
print(f"Resultado do método de Taylor de primeira ordem: {resultado_taylor_primeira_ordem}")
