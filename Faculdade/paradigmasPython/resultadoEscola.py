# Implementar um programa em python que resolva as seguintes questões:
    # Se a nota for MAIOR OU IGUAL a 7, o estudante foi aprovado;
    # Se a nota for MENOR que 7 e MAIOR OU IGUAL a 5, o estudante  está de recuperação;
    # Se a nota for MENOR que 5, o estudante está reprovado.

n1 = float(input("AV 1: "))
n2 = float(input("AV 2: "))
n3 = float(input("AV 3: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f"Média final {media:.2f}, estudante aprovado")
elif media < 7 and media >= 5:
    print(f"Média final {media:.2f}, estudante de recuperação")
else:
    print(f"Média final {media:.2f}, estudante reprovado")