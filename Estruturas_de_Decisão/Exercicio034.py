#Faça um programa que calcule as raízes de uma equação do segundo graua, na forma ax² + bx + c
#O programa deverá pedir os valores de a,b e c e fazer as consistências, informando ao usuário nas seguintes situações:
import math

a = float(input('Insira o valor de A: '))
if a == 0:
    print('A equação não é do segundo grau')
else:
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))
    delta = (b**2) - 4 * a * c
    if delta < 0:
        print('A equação não possui raizes')
    elif delta == 0:
        x1 = -b/(2*a)
        print(f'A equação possui apenas uma raiz, x = {x1}')
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f'A equação possui duas raizes, x1 = {x1}, x2 = {x2}')
        
