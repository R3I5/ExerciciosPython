# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada
# Consdidera que a covertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
import math

area = float(input("Insira o tamanho em metros da área a ser pintada:"))

qTinta = area/54
qLatas = math.ceil(qTinta)
precoTotal = qLatas * 80

print(f"Serão necessárias {qLatas} latas de tinta")
print(f"O valor total será {precoTotal} R$")

#biblioteca math para importar a função math.ceil(arredonda para cima) e a função math.floor(arredonda para baixo)