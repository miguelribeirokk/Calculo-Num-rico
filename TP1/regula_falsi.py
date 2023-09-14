import math


def f(x):
    return x ** 3 + 3 * x ** 2 - 1


def metodo_regula_falsi(a, b, tolerancia, max_iteracoes):
    iteracoes = 0

    while iteracoes < max_iteracoes:
        fa = f(a)
        fb = f(b)

        if math.fabs(fa) < tolerancia:
            print("A raiz é:", a)
            return

        if math.fabs(fb) < tolerancia:
            print("A raiz é:", b)
            return

        xn = a - (fa * (b - a)) / (fb - fa)

        if math.fabs(f(xn)) < tolerancia:
            print("A raiz é:", xn)
            return

        if f(a) * f(xn) < 0:
            b = xn
        else:
            a = xn

        iteracoes += 1

    print("O método não convergiu após", max_iteracoes, "iterações.")


def main():
    a = float(input("Primeiro ponto inicial (a): "))
    b = float(input("Segundo ponto inicial (b): "))
    tolerancia = 1e-5
    max_iteracoes = 100

    metodo_regula_falsi(a, b, tolerancia, max_iteracoes)


if __name__ == "__main__":
    main()
