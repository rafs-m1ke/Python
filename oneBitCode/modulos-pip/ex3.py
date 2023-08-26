import re
# Escrever um programa em python para vrificar se uma string contém apenas um determinado
# conjunto de caracteres (neste caso, a-z, A-Z e 0-9).

def string_verifier(string):
    RULE = re.compile(r"^a-zA-Z0-9")
    string = RULE.search(string)
    return not bool(string)
    
print(string_verifier("ASGDVAHJSDJBasdgjhkeb15623817"))
