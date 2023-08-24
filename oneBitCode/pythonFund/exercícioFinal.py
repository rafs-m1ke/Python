"""
## Gerenciamento de Jogadores e Times

Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time
1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.
"""
teams = {}
done = False

# função para listar times
def printTeams():
    print("Times Listados: ")
    for i, team in enumerate(teams.values()):
        print(f"{i + 1}. {team['name']} ({len(team['players'])} jogadores)")

# função para listar jogadores de um time
def printTeamPlayers():
    print(f"Jogadores do time {teams['name']}")
    for i, player in enumerate(teams['players']):
        print(f"{i+1}. {player}")
    
while not done:
    # Opções no programa
    print('''
Oque deseja fazer?
1. Adicionar um time
2. Remover um time
3. Listar um time
4. Adicionar jogador em um time
5. Remover jogador de uma time
6. Listar jogadores de um time
7. Sair
          ''')
    
    choice = input("> ")
    if choice == "1":
        teamName = input("Digite o nome do time: ")
        teams[teamName] = {"name" : teamName, "players" : []}
    if choice == "2":
        printTeams()
        teamNum = int(input("Informe o número do time a ser removido: "))
        if teamNum <= len(teams):
            teamName = list(teams.keys())[teamNum - 1]
            del teams[teamName]
        else:
            print("Número do time inválido!")
    if choice == "3":
        printTeams()
    if choice == "4":
        printTeams()
        teamNum = int(input("Informe o numero do time onde deseja adicionar o jogador: "))
        if teamNum <= len(teams):
            teamName = list(teams.keys())[teamNum - 1]
            playerName = input("Informe o nome do jogador: ")
            teams[teamName]["players"].append(playerName)
            print("Jogador adicionado no time")
        else:
            print("Número do time está inválido")
    if choice == "5":
        printTeams()
        teamNum = int(input("Informe o número do time que deseja remover o jogador: "))
        if teamNum <= len(teams):
            teamName = list(teams.keys())[teamNum -1]
            printTeamPlayers(teams[teamName])
            playerNum = int(input("Informe o número do jogador que deseja remover: "))
            if playerNum <= len(teams[teamName]['players']):
                del teams[teamName]['players'][playerNum - 1]
                print("Jogador removido do time")
            else:
                print("Número do jogador inválido!")
        else:
            print("Número do time inválido!")
    if choice == "6":
        printTeams()
        teamNum = int(input("Informe o numero do time onde deseja listar o jogador: "))
        if teamNum <= len(teams):
            teamName = list(teams.keys())[teamNum - 1]
            printTeamPlayers(teams[teamName])
        else:
            print("Numero do time inválido")
    if choice == "7":
        done = True
    else:
        print("Opção inválida")