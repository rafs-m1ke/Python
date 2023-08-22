"""
Aumento salário funcionário
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""
salario = float(input("Digite o valor do salário: "))

if salario > 1250:
    salario += salario * 0.10
    print(f"Salario final de R$ {salario:.2f}, com aumento de 10%")
else:
    salario += salario * 0.15
    print(f"Salario final de R$ {salario:.2f}, com aumento de 15%")
    