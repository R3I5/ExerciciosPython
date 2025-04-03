#Faça um programa que leia um número inteiro maior que 0 e menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do 'e', da vírgula entre outros

numero = float(input('Insira o número desejado: '))
if 0 > numero >= 1000:
    print('Número inválido')
else:
    unidade = numero % 10
    dezena = (numero % 100) // 10
    centena = numero // 100
    separador1 = ","
    separador2 = ""
    