#Faça um programa que peça o tamanho de um arquivo para dowload (em MB) e a velocidade de um link da Internet(em Mbps)
#calcule e informe o tempo aproximado de download do arquivo usando este link(em minutos)

arquivo = float(input("Insira o tamanho do arquivo em MB:"))
velocidade = float(input("Insira o a velocidade de download em Mbps:"))

tempoDownload = (arquivo*8)/velocidade
minutos = tempoDownload // 60
segundos = tempoDownload % 60

print(f"O arquivo levará {minutos:.0f} minutos e {segundos:.0f} segundos para ser baixado")