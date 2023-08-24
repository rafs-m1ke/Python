"""
*args - Utilizamos ele quando não temos certeza de quantos argumento queremos ter numa função
- Os argumentos são passados como uma tupla

**kwargs - Alem dos valores, podemos passar também as respectivas chaves para cada argumento
- Os argumentos são passados como um dicionário
"""

# 1- Soma de números
def sum(*num):
    sumTotal = 0
    for n in num:
        sumTotal += n
    print(f"Soma é: {sumTotal}")
    
sum(7, 9, 10, 11)

# 2- Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

presentation(name="Python", category="BackEnd", level="Iniciante")