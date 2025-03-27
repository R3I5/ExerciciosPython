# Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno

turno = input("Em qual turno você estuda? Digite M para matutino, V para vespertino e N para noturno:")
if turno == 'M' or turno == 'm':
    print("Bom dia!")
elif turno == 'V' or turno == 'v':
    print("Boa tarde!")
elif turno == 'N' or turno == 'm':
    print("Boa noite!")
else:
    print("Entrada inválida")
