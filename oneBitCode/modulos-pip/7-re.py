import re

TEXT = "OneBitCode: Tranformamos pessoas em programadores sem limites"

# 1- Índice inicial e final de palavras
# O "r" significa que estamos trabalhando com uma string bruta (row string)
match = re.search(r"pessoas em programadores", TEXT)
print("Índice inicial ", match.start())
print("Índice final ", match.end())

# 2- Buscando o índice que possui o ponto
SITE = "https://onebitcode.com"
# match = re.search(r".", SITE)
match = re.search(r"\.", SITE)
print(match)

# 3- Buscando uma lista de caracteres dentro de uma frase
PATTERN = "[a-m]"
RESULT = re.findall(PATTERN, TEXT)
print(TEXT)
print(RESULT)

# 4- Verificando o início de uma string
RULE = r"^A"
PHRASES = ["A casa está suja", "O dia está lindo", "Vamos passear"]
for f in PHRASES:
    if re.match(RULE, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")

# 5- Verificando o final de uma string
RULE_END = r"!$"
PHRASES2 = "O dia está lindo"
match = re.search(RULE_END, PHRASES2)
if match:
    print("Sim, corresponde")
else:
    print("Não corresponde")