import statistics

# 1- Aplicar a média
lista1 = [3, 2, 3, 8, 9]
print(f"A média de {lista1} é {statistics.mean(lista1)} ")

# 2- Aplicar a mediana
lista2 = [1, 2, 3, 7, 8, 9]
print(f"A mediana de {lista1} é {statistics.median(lista1)}")
print(f"A mediana de {lista2} é {statistics.median(lista2)}")

# 3- Aplicar a moda
lista3 = [2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]
print(f"A moda de {lista3} é {statistics.mode(lista3)}")

# 4- Desvio padrão
# Quanto mais próximo de 0 for o desvio padrão, os dados estão menos dispersos

print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))
