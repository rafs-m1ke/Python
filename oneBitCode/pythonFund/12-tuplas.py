gamesTuple = ("Fifa 23", "Star Wars", "Mario Odyssey", "The Legend of Zelda")
print(gamesTuple)
print(type(gamesTuple))

# Tupla não possibilita adicionar, remover ou ordenar valores
# É possivel buscar informações por meio do slice

# 1- Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2- Buscar o último iten da lista
print(gamesTuple[-1])

# 3- Buscar até uma determinada posição
print(gamesTuple[:3])

# 4- Buscar jogos de uma posição em diante
print(gamesTuple[1:])

# 5- Recuperar um iten da tupla pelo indice
print(gamesTuple.index("Mario Odyssey"))