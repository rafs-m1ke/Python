def welcome():
    print("Hello World")

welcome()

# 2- Função para somar dois números
def sum(x,y):
    print(x + y)
    return x + y

sum(5,4)

# 3- Função para cadastrar um jogo
def createGame():
    name = input("Digit o nome do jogo: ")
    yearLaunch = int(input("Digite o ano de lançamento: "))
    gamePrice = float(input("Digite o preço do jogo: "))
    noteRating = float(input("Nota de anvaliação: "))
    
    print(f"{name} - R$ {gamePrice:.2f}")
    
createGame()