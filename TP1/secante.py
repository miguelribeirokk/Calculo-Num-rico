import math


def f(x):
    return x ** 3 - 9 * x + 3


def metodo_secante(x0, x1, tolerancia, max_iteracoes):
    iteracoes = 0

    while iteracoes < max_iteracoes:
        if math.fabs(f(x1)) < tolerancia:
            print("A raiz é:", x1)
            return

        xn = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        x0 = x1
        x1 = xn
        iteracoes += 1

    print("O método não convergiu após", max_iteracoes, "iterações.")


def main():
    x0 = float(input("Primeira estimativa: "))
    x1 = float(input("Segunda estimativa: "))
    tolerancia = 1e-5
    max_iteracoes = 100

    metodo_secante(x0, x1, tolerancia, max_iteracoes)


if __name__ == "__main__":
    main()
