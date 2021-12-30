import socket

url = input("insira a URL que deseja testar: ")

caminhos = open('wordlist.txt', 'r')

for caminho in caminhos:
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.settimeout(0.5)
    retorno = url + '/' + caminho.strip()
    url = retorno
    print(retorno)
    conecta = conexao.connect((url, 80))
    