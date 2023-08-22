# Substituindo caractere repetido

name = input("Digite um texto qualquer: ")

char = name[0].lower() # Reserva a primeiro caractere da string em uma variável, transformando em minúsculo
newName = name.replace(char, '$') # reserva a string inicial, substituido a string anterior - variável "char"
finalName = char + newName[1:]
print(finalName)