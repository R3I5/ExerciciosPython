#Faça um programa que leia três números e mostre o maior e o menor deles

numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
numero3 = float(input("Digite o terceiro numero:"))

def maior(numero1, numero2, numero3):
    if numero1>numero2 and numero3:
        return numero1
    elif numero2>numero1 and numero3:
        return numero2
    else:
        return numero3
        
def menor(numero1, numero2, numero3):
    if numero1<numero2 and numero1< numero3:
        return numero1
    elif numero2<numero1 and numero2< numero3:
        return numero2
    else:
        return numero3

print(f"O maior número é: {maior(numero1,numero2,numero3)}")
print(f"O menor número é: {menor(numero1,numero2,numero3)}")
