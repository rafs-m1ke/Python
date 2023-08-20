gameName = "Fifa 23"
gameDescription = """
    Fifa 23 é um jogo de futebol, desenvolvido
    pela EA Sports, que possibilita jogar online
    ou localmente
"""
print(gameName.upper()) # Retornar String em Maiúsculo
print(gameName.lower()) # Retornar String em Minúsculo
print(gameName.capitalize()) # Retornar String com a primeira letra em Maiúsculo - ou .title() -> Mesmo resultado
print(gameName.center(11, '-')) # Retorna String Centralizada com Caractere de Preenchimento
print(gameName.find('a')) # Retorna a posição (índice) de uma determinado caractere
print(gameDescription.count("f")) # Conta a quantidade de caracteres
print(gameDescription.count("a"))
print(gameDescription.replace("Fifa", "PES")) # Substitui uma string por outra
print(gameDescription.split(","))