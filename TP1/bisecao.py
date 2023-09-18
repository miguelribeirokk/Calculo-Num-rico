import math


# Basta mudar a f(x) para a função desejada
def f(x):
    return x ** 2 - 3

def check(a, b):
    return f(a) * f(b) < 0

def metodo_bissecao(a, b, e):
    if not check(a, b):
        print("Intervalo não contém raiz.")
        return
    
    i = 0
    xi = (a + b) / 2  # Inicialização de xi
    while math.fabs((b - a) / 2) > e or i < 3:
        if f(xi) == 0:
            print("A raiz é:", xi)
            print("Erro:", math.fabs((b - a) / 2) - xi)
            break
        else:
            if f(a) * f(xi) < 0:
                b = xi
            else:
                a = xi
            xi = (a + b) / 2  # Atualização de xi
        i += 1

    if i >= 3:
        print("A raiz é aproximadamente:", xi)
        print("Erro:", math.fabs((b - a) / 2))

def main():
    a = float(input("Início do intervalo: "))
    b = float(input("Fim do intervalo: "))
    e = 0.01

    metodo_bissecao(a, b, e)


if __name__ == "__main__":
    main()
