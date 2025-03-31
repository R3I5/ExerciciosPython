# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule sua média
# A atribuição de conceitos obedece à tabela abaixo: Média A B C D E 
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem de APROVADO se o conceito foi A B C ou o conceito de REPROVADO se o conceito for D ou E

notaParcial1 = float(input('Insira a primeira nota parcial: '))
notaParcial2 = float(input('Insira a segunda nota parcial:')) 

media = (notaParcial1+notaParcial2)/2

if 9.0 <= media <= 10.0:
    print(f'Conceito A, Aluno APROVADO com média: {media:.2f}')
elif 7.5 <= media < 9.0:
    print(f'Conceito B, Aluno APROVADO com média: {media:.2f}')
elif 6.0 <= media < 7.5:
    print(f'Conceito C, Aluno APROVADO com média: {media:.2f}')
elif 4.0 <= media < 6.0:
    print(f'Conceito D, Aluno REPROVADO com média: {media:.2f}')
elif 0 <= media < 4.0:
    print(f'Conceito E, Aluno REPROVADO com média: {media:.2f}')