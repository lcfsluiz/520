#!/usr/bin/python3

qtd = int (input('Quantidade de notas: '))

soma = 0
for x in range(qtd):
    nota = float(input('Digite n{}: '.format(x+1)))
    soma += nota

media = soma / qtd 

if media >= 7:
    print("Aprovado, media: {}".format(media))
elif media > 3:
     print('recuperação, media: {}'.format(media))
else:
    print('reprovado, media: {}'.format(media))