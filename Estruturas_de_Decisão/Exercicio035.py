#Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é bissexto ou não

ano = int(input('Insira o ano desejado: '))
if ano%4 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')