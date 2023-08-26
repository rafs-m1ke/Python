"""
Módulo para tratar algumas strings e que possua as seguintes funcionalidades:
1. Inverter uma string de trás pra fente;
2. Retornar apenas letras com índice par;
3. Retornar apenas letras com índice ímpar.
"""


def inverse(string):
    contrarian = string[::-1]
    return contrarian


def oddIndex(index):
    odd = index[0::2]
    return odd


def pairIndex(index):
    pair = index[1::2]
    return pair
