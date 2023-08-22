"""
Cálculo da Distância
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.
"""

dist = float(input("Qual a distância a ser percorrida? (km) "))

if dist <= 200:
    tarifa = 0.50
    passagem = tarifa * dist
else:
    tarifa = 0.35
    passagem = tarifa * dist
    
print(f"O valor da passagem para {dist} Km, com tarifa de {tarifa}, é R$ {passagem:.2f}")