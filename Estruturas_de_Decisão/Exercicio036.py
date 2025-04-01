data = input('Digite uma data no formato dd/mm/aaaa: ')
dia, mes, ano = data.split("/")
dia, mes, ano = int(dia), int(mes), int(ano)

if ano < 0:
    print('Ano inválido!')
elif mes < 1 or mes > 12:
    print('Mês inválido!')
else:
    # Definição do número de dias de cada mês
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    else:  # Fevereiro
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):  # Ano bissexto
            max_dias = 29
        else:
            max_dias = 28

    if 1 <= dia <= max_dias:
        print('Data válida!')
    else:
        print('Dia inválido!')
