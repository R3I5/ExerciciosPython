#Faça um programa que verifique se uma letra digitada é "F" ou "M"
#Conforme a letra escrever: F - feminino, M - masculo, Sexo inválido.abs

sexo = input("Insira seu sexo: F(Para feminino) e M(Para masculino):")
if sexo == 'M' or sexo == 'm':
    print("M - Masculino")
elif sexo == 'F' or sexo == 'f':
    print("F - Feminino")
else:
    print("Sexo inválido")

