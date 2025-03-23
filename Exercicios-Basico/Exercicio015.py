#Faça um programa que caclule quanto você ganha por hora e o número de horas trabalhadas por mês
#Calcule e mostre o total do seu salário referido mês, sabendo-se que são descontados 11% para o imposto de renda
#8% para o INSS  e 5% para o sindicato, faça um programa que nos dê: salário bruto, quanto pagou ao INSS. qunato pagou ao sindicato. o salário bruto. calcule os descontos e o salário liquido.

salarioHora = float(input("Insira quanto você ganha por hora:"))
horasTrabalhadas = float(input("Insira quantas horas foram trabalhadas:"))

salarioBruto = salarioHora * horasTrabalhadas

ir = salarioBruto * (0.11)
inss = salarioBruto * (0.08)
sindicato = salarioBruto * (0.05)

print(f"+ Salário Bruto : {salarioBruto} R$")
print(f"- IR (11%) : {ir} R$")
print(f"- INSS (8%) : {inss} R$")
print(f"- Sindicato (5%) : {sindicato} R$")

salarioLiquido = salarioBruto - ir - inss - sindicato

print(f"= Salário Liquído : {salarioLiquido} R$")
