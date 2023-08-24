# Implementar uma solução que calcule o fatorial de um número
def fatorial(x):
    if x == 0 or x == 1:
        return 1
    return x * fatorial(x - 1)

print(fatorial(5))