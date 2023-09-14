import math


def f(x):
    return x ** 3 - 2 * x - 5


def g(x):
    return (2 * x + 5) ** (1 / 3)


def metodo_ponto_fixo(x0, tolerancia, max_iteracoes):
    iteracoes = 0

    while iteracoes < max_iteracoes:
        x1 = g(x0)
        if math.fabs(f(x1)) < tolerancia:
            print("A raiz é:", x1)
            return

        x0 = x1
        iteracoes += 1

    print("O método não convergiu após", max_iteracoes, "iterações.")


def main():
    x0 = float(input("Estimativa inicial: "))
    tolerancia = 1e-5
    max_iteracoes = 100

    metodo_ponto_fixo(x0, tolerancia, max_iteracoes)


if __name__ == "__main__":
    main()
