#!/usr/bin/python/3
meses = ('janeiro', 'feveiro', 'março', 'abril', 'maio', 'junho', 'julho', 'julho', 'agosto', 'setembro', 'outrubro', 'novembro', 'dezembro')

data_nasc = input('Digite sua data de nascimento DD-MM-AAAA: ')
indice = int(data_nasc[3:5])
mes = meses[indice]
print('você nasceu no mês' ,mes)
