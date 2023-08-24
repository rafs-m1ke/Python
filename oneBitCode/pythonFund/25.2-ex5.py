# Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
def pairOddSeparator(x=True):
    pairs = []
    odd = []
    while x == True:
        entrada = input("Digite um número (x para sair): ")
        if eval(entrada) % 2 == 0:
            number = eval(entrada)
            pairs.append(number)
        elif eval(entrada) % 2 == 1:
            number = eval(entrada)
            odd.append(number)
        else:
            x = False

    print(pairs)
    print(odd)

pairOddSeparator()