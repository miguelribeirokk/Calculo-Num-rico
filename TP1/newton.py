import math

def f(x):
    return x**3 - 2*x + 1

def derivada(x):
    return 3*x**2 - 2


def metodo_newton(x0, tolerancia, max_iteracoes):
    iteracoes = 0

    while iteracoes < max_iteracoes:
        fx0 = f(x0)
        if math.fabs(fx0) < tolerancia:
            print("A raiz é:", x0)
            return

        f_derivada_x0 = derivada(x0)
        if f_derivada_x0 == 0:
            print("A derivada é zero. O método de Newton falhou.")
            return

        xn = x0 - fx0 / f_derivada_x0

        if math.fabs(f(xn)) < tolerancia:
            print("A raiz é:", xn)
            return

        x0 = xn
        iteracoes += 1

    print("O método não convergiu após", max_iteracoes, "iterações.")

def main():
    x0 = float(input("Estimativa inicial: "))
    tolerancia = 1e-5
    max_iteracoes = 100

    metodo_newton(x0, tolerancia, max_iteracoes)

if __name__ == "__main__":
    main()
