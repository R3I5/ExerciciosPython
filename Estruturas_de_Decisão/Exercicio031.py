# Faça um programa que leia um número e exiba o dia correspondente da semana
#(1 - Doming, 2 - Segunda,etc). se digitar outro valor deve aparecer valor inválido

dia = int(input('Digite o número do dia da semana desejado: '))

if dia == 1:
    print(f'O dia correspondente a {dia} é o Domingo')
elif dia == 2:
    print(f'O dia correspondente a {dia} é a Segunda')
elif dia == 3:
    print(f'O dia correspondente a {dia} é a Terça')
elif dia == 4:
    print(f'O dia correspondete a {dia} é a Quarta')
elif dia == 5:
    print(f'O dia correspondete a {dia} é a Quinta')
elif dia == 6:
    print(f'O dia correspodente a {dia} é a Sexta')
elif dia == 7:
    print(f'O dia correspondete a {dia} é o Sabado')
else:
    print('Valor inválido')