# 1- Crie uma finção que receba dois argumentos: o primeiro nome e o ultimo nome
def fullName(fname, lname):
    print(f"Nome completo: {fname} {lname}")

fullName("Rafael", "Silva")

# 2- Crie uma função  que some dois números via argumetos
def sum(a, b):
    return a + b

print(sum(10, 50))

# 3- Argumentos default em uma função
def address(country="Brasil"):
    print(f"Eu moro no {country}")

address()
address("Canadá")

# 4- Avaliação de jogo
def ratingGame(qtdRating):
    gameName = input("Digite o nome do jogo: ")
    sum = 0 
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo: "))
        sum += note
    print(f"Média de avaliação do jogo {gameName} é: {sum / qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo: "))
ratingGame(rating)