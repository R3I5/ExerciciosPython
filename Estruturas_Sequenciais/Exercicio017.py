#faça um programa para uma loja de tintas
#O programa deverá pedir o tamanho em petros quadrados da área a ser pintada
#Considere que a coberta da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros
#Que custam R$ 80,00 ou em galões de 3,6 litros, que custam 25,00
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações

import math

area = float(input("Insira o tamanho em metros da área a ser pintada:"))

areaMais10 = area * 1.0
coberturaTinta = 6
latasLitros = 18
latasPreco = 80.00
latasRendimento = latasLitros*coberturaTinta
galoesLitros = 3.6
galoesPreco = 25.00
galaoRendimento = galoesLitros*coberturaTinta

apenasLatasQnt = math.ceil(area/latasRendimento)
apenasLatasPreco = apenasLatasQnt * latasPreco
latas = math.floor(areaMais10 / latasRendimento)

apenasGaloesQnt = math.ceil(area/galaoRendimento)
apenasGaloesPreco = apenasGaloesQnt * galoesPreco
galoes = math.ceil(areaMais10 % latasRendimento) / galaoRendimento

LatasGaloesPreco = ((latas*apenasLatasPreco) + (galoes * apenasGaloesPreco))

print(
    f"Quantidade de latas: {math.ceil(apenasLatasQnt)} \n"
    f"Preço com apenas latas: {apenasLatasPreco:.2f} R$ \n"
    f"Quantidade de galões: {math.ceil(apenasGaloesQnt)} \n"
    f"Preço com apenas galões: {apenasGaloesPreco:.2f} R$ \n"
    f"Quantidade de latas: {math.ceil(latas)}, quantidade de galões: {math.ceil(galoes)} \n"
    f"Preço com latas e galões: {LatasGaloesPreco:.2f} R$"
)