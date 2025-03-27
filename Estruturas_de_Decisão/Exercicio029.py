#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salarioBase = float(input("Insira seu salário atual:"))
if salarioBase <= 280.00:
    salarioNovo = (salarioBase + (salarioBase*0.2))
    aumento = salarioNovo - salarioBase
    print(f"Salario base:{salarioBase}")
    print("O percentual de aumento foi de:20%")
    print(f"O valor do aumento foi de:{aumento}")
    print(f"O seu novo salário é:{salarioNovo}")
    
elif 280.0 > salarioBase <700.00:
    salarioNovo = (salarioBase + (salarioBase*0.15))
    aumento = salarioNovo - salarioBase
    print(f"Salario base:{salarioBase}")
    print("O percentual de aumento foi de:15%")
    print(f"O valor do aumento foi de:{aumento}")
    print(f"O seu novo salário é:{salarioNovo}")
    
elif 700.0 > salarioBase < 1500.00:
    salarioNovo = (salarioBase + (salarioBase*0.10))
    aumento = salarioNovo - salarioBase
    print(f"Salario base:{salarioBase}")
    print("O percentual de aumento foi de:10%")
    print(f"O valor do aumento foi de:{aumento}")
    print(f"O seu novo salário é:{salarioNovo}")
    
else:
    salarioNovo = (salarioBase + (salarioBase*0.05))
    aumento = salarioNovo - salarioBase
    print(f"Salario base:{salarioBase}")
    print("O percentual de aumento foi de:5%")
    print(f"O valor do aumento foi de:{aumento}")
    print(f"O seu novo salário é:{salarioNovo}")

