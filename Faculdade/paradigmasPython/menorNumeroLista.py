def encontrarMinimoLista(lista):
    minimo = lista[0]
    for elem in lista:
        if elem < minimo:
            minimo = elem
    return minimo

listaTeste = [2, 10, 3, 1, 4, 5]
menor = encontrarMinimoLista(listaTeste)
print(f"O menor elemento da lista é: [{menor}]")