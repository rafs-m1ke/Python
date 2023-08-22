gameList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1- Iterando valores de uma lista
# for game in gameList:
#     print(game)

# 2- Quando a condição for atendida, o Loop será encerrado
# for game in gameList:
#     if game == "Red Dead 2":
#         break
#     print(game)
    
# 3- Quando a condição for atendida, o loop vai para a proxima iteração
# for game in gameList:
#     if game == "Red Dead 2":
#         continue
#     print(game)
    
# 4- Avaliação do Jogo
gameName = input("Digite o nome do jogo: ")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo: "))
sum = 0

for i in range(gameRating):
    note = float(input("Digite a nota para o jogo: "))
    sum += note
    
print(f"Média de avaliação do jogo \"{gameName}\" é {sum / gameRating:.2f}")