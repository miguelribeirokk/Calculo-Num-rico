def binario_para_decimal(binario):
    return int(binario, 2)


def decimal_para_binario(decimal):
    return bin(decimal)[2:]


def main():
    print("Decimal ou Binário?")
    print("1 - Decimal")
    print("2 - Binário")
    op = int(input("Opção: "))
    if op == 1:
        decimal = int(input("Digite o número decimal: "))
        print("Binário: ", decimal_para_binario(decimal))
    elif op == 2:
        binario = input("Digite o número binário: ")
        print("Decimal: ", binario_para_decimal(binario))
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
