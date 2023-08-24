# Implementar um programa que some todos os numeros pares de uma lista
    # Exemplo: Se a lista for [10, 2, 5, 7, 6, 3], o resultado deve ser igual a 18!
    
lista = [10, 2, 5, 7, 6, 3]
soma = 0

for i in lista:
    if i % 2 == 0:
        soma += i

print(soma)