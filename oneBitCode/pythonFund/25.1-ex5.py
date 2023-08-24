# Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.
text = input("Digite uma string: ")

def upperLowerCounter(x):
    type = {"Uppercase" : 0, "Lowercase" : 0}
    for i in x:
        if i == i.upper():
            type["Uppercase"] += 1
        elif i == i.lower():
            type["Lowercase"] += 1
    print(f"A string contém {type}!")

upperLowerCounter(text)
            