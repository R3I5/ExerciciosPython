import requests

# Definindo o usuário que queremos buscar
usuario = "Arture07"

# Montando a URL da API
url = f"https://api.github.com/users/{usuario}"

# Fazendo a requisição GET
resposta = requests.get(url)

# Verificando se deu certo
if resposta.status_code == 200:
    dados = resposta.json()  # Convertendo o JSON para um dicionário Python
    print(f"Nome: {dados['name']}")
    print(f"Bio: {dados['bio']}")
    print(f"Repositórios Públicos: {dados['public_repos']}")
else:
    print("Erro ao buscar informações do usuário.")
