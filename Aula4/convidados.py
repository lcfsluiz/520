#!/usr/bin/python/3
convidados = []

def adicionar(nome):
    '''função para adicionar convidados na lista'''
    global convidados
    convidados = {'nome': nome, 'idade': idade}
    convidados.append(nome)
    return True



while True
    nome = input('Digite um nome ou sair: ')
    if nome.strip().lower() == 'sair':
        break 
    idade = int(input('Digite a idade: '))
    adicionar(nome, idade)

print(convidados)