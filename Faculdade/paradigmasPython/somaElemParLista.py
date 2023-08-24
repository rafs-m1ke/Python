# Implementar um asolução em python que retorne a soma de todos os elemntos pares em uma lista

def total_soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
        else:
            pass
    return soma


listaTeste = [0, 4, 6, 9, 3, 2]
resultant = total_soma_par(listaTeste)
print(f'A soma de todos os elementos pares da lista {listaTeste} é {resultant}')
