# Implementar um solução que resolva a seguinte questão
    # Calcular o valor de uma compra, sendo que o preço unitário é R$ 10,00
    # Se for feita uma compra de até 10 unidades, não há descontos
    # Para compras entre 11 e 20 unidades é dado um desconto de 10%
    # Acima de 20 unidades, é dado um desconto de 20%
    
print("Valor do produto: R$ 10,00")
qnt = int(input("Quantos deseja comprar? "))
valor = 0
desconto = 0

if qnt <= 10:
    valor = qnt * 10
elif qnt > 10 and qnt <= 20:
    desconto = 0.10
    valor = qnt * 10
    valor -= valor * desconto
else:
    desconto = 0.20
    valor = qnt * 10
    valor -= valor * desconto

print(f"O preço total de {qnt} produtos e {desconto * 100:.0f}% de desconto, é de R$ {valor:.2f}")