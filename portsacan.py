#TODO inserir um input que transforma em array
#TODO por em  um for e depois juntar ese codigo em um menu

import socket

def conexao(url, porta):
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.settimeout(0.5)
    resposta = conexao.connect_ex((url, int(porta)))
    return resposta


url = input('insira a URL para verificar: ')
portas = input("Insira as portas que deseja verificar separadas por virgula: ").replace(" ","").split(',')


for porta in portas:
    resposta = conexao(url, int(porta))
    if resposta == 0:
        print('porta:', porta, '200 SUCESS')
    elif resposta != 0:
       print("porta:", porta, "FECHADA")
    