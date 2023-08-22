gamesSet = {"Fifa 23", "Red Dead Redemption 2", "Star Wars", "The Legend of Zelda", "Mario Odyssey", "Resident Evil 4"}
print(gamesSet)

# Não possibilita recuperar valores via fatiamento ou slice

# 1- Buscar o tamanho do set
print(len(gamesSet))

# 2- True e 1 são considerados o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3- Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4- Remover itens do set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)
