##Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

produto1 = float(input("Por favor, insira o valor do primeiro produto:"))
produto2 = float(input("Por favor, insira o valor do segundo produto:"))
produto3 = float(input("Por favor, insira o valor do terceiro produto:"))

if produto1 < produto2 and produto1 < produto3:
    print("Você deve comprar o primeiro produto") 
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve comprar o segundo produto")
else:
    print("Você deve comprar o terceiro")