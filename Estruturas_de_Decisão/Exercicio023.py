#Faça um programa para a leiturua de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete
#A mensagem reprovado se a média for menor do que sete: A mensagem "Aprovado com distinção" se a média for igual a dez

nota1 = float(input("Insira a primeira nota do aluno:"))
nota2 = float(input("Insira a segunda nota do aluno:"))

media = (nota1+nota2)/2

if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
