##Faça um programa que pergunte quanto voce ganha por honra e o numero de horas trabalhadas no mes. Calcule e mostre o total do seu salario no referido mes

salario = float(input("Qual o valor recebido por hora?"))
horas = int(input("Quantas horas foram trabalhadas no mês?"))
salariototal = salario * horas
print(f"O salario referido no mês é:{salariototal}")
