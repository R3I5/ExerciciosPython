#Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equiilátero, isósceles ou escalenos

lado1 = float(input('Informe o tamanho do primeiro lado do triângulo: '))
lado2 = float(input('Informe o tamanho do segundo lado do triângulo: '))
lado3 = float(input('Informe o tamanho do terceiro lado do triângulo: '))

if lado1 + lado2 == lado3:
    print('Tamanhos inválidos')
elif lado2 + lado3 == lado1:
    print('Tamanhos inválidos')
elif lado3 + lado1 == lado2:
    print('Tamanhos inválidos')
else:
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Triângulo Isósceles')
    elif lado1 != lado2 or lado2 != lado3 or lado1 != lado3:
        print('Triângulo Escaleno')