#!/usr/bin/python3
idade = input('digite sua idade: ')

if idade.isnumeric():
    if int(idade) >= 18:
        print('Permitido')
    else:
        acom = input("Está acompanhado: s/n: ")
        if  acom.lower() == 's':
            result = 'Permito Com acompanhate'
        else:
            result = 'Acesso negado!'

else:
    print("Não é possivel converter")
