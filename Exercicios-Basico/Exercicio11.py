#Faça um produto que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro
#do primeiro com metade do segundo. A soma do triplo do primeiro com o terceiro e o terceiro elevado ao cubo

inteiro1 = int(input("Digite o primeiro numero inteiro:"))
inteiro2 = int(input("Digite o segundo numero inteiro:"))
real = float(input("Digite o numero real:"))

resultado1 = ((inteiro1*2)*(inteiro2/2))
resultado2= ((inteiro1*3)+real)
resultado3 = (real**3)

print(f"O primeiro resultado é:{resultado1}")
print(f"O segundo resultado é:{resultado2}")
print(f"O terceiro resultado é:{resultado3}")