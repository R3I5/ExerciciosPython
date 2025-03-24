#João Papo-de-Pescador. homen de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de são paulo(50 quilos)
#deve pagar uma multa de 4,00 por quilo excedente
#João precisa que você faça um programa que leia a variável peso e calcule o excesso
#Gravar na variável excesso a quantidade de quilos além do limite e na variável o valor da multa que João devera pagar
#Imprima os dados do programa com as mensagens adequadas

peso = float(input("Insira quantos quilos de peixe foram pescados:"))
excesso = peso - 50
multa = excesso * 4

print(f"Foram pescados {excesso} quilos de peixem excedentes")
print(f"O valor da multa a ser pago é {multa} reais")
