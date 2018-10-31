#!/usr/bin/python/3

def ler_arquivo(teste):
    with open(teste, 'r') as arq:
        return arq.readlines()


def escrever_arquivo(teste, conteudo):
    with open(teste, 'a') as arq:
        arq.write.(conteudo + '\n')