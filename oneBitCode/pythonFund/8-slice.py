gameName = "Fifa 23"
gameDescription = """
    Fifa 23 é um jogo de futebol, desenvolvido
    pela EA Sports e que possibilita jogar online
    ou localmente
"""

# Fatiamento de string -> string[início:fim:passo] - índice começa na posição 0 | índice final -1
# Passo - determina o incremento. Por padrão é o número 1

# 1- Busque toda string a partir da primeira posição
print(gameName[0:]) 

# 2- Busque toda string até a última posição
print(gameName[:7])

# 3- Busque toda string da terceira até a última posição
print(gameName[2:])

# 4- Busque toda string de 2 em 2 caracteres
print(gameName[::2])

# 5- Busque todas as strings nos índices ímpares
print(gameName[1::2])

# 6- Inverter uma string de trás para frente
print(gameName[::-1])