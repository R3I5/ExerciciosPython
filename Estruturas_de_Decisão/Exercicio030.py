# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto(conforme tabela abaixo) e 10% para o inss e que o fgts corresponde a 11% do salário bruto, mas não é descontado

horas = float(input('Insira quantas horas são trabalhadas: '))
valorHora = float(input('Insira o valor por hora: '))
salarioBruto = horas * valorHora
impostoRenda = 0
if salarioBruto <= 900:
    impostoRenda = 0
elif 900 < salarioBruto <= 1500:
    impostoRenda = (salarioBruto*0.05)
elif 1500 < salarioBruto <= 2500:
    impostoRenda = (salarioBruto*0.1)
else:
    impostoRenda = (salarioBruto * 0.2)
INSS = (0.1 * salarioBruto)
FGTS = (0.11 * salarioBruto)
descontosTotais = INSS + impostoRenda
salarioLiquido = salarioBruto - descontosTotais
print(f'Salario Bruto: ({horas} * {valorHora}: R$ {salarioBruto:.2f})')
print(f'(-) IR (5%): R$ {impostoRenda:.2f}')
print(f'(-) INSS (10%): R$ {INSS:.2f}')
print(f'FGTS (11%): R$ {FGTS:.2f}')
print(f'Total de descontos: R$ {descontosTotais:.2f}')
print(f'Salário Liquído: R$ {salarioLiquido:.2f}')
