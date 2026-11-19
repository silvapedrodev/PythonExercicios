import requests

url = "https://pudim.com.br/"

try:
    resposta = requests.head(url, timeout=5)
    print("Consegui acessar so site Pudim com sucesso!")
except:
    print("O site Pudim não está acessível no momento.")
