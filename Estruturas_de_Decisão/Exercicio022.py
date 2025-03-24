#Faça um programa que verifique se uma letra digitada é vogal ou consoante

letra = input("Insira a letra desejada:").upper()

if(
    letra == "A"
    or letra == "E"
    or letra == "I"
    or letra == "O"
    or letra == "U"
):
    print("Vogal")
else:
    print("Consoante")
