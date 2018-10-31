try:
    n = input('Digite um numero: ')
    n = int(n)
    if n % 2 == 0:
         print('par')
    else:
        print('impar')


except ValueError:
    res = [ord(x) for in n]
    res = sum(res)
    if res % 2 == 0:
        print('par {}' .format(res))
    else:
    print('par {}' .format (res))

except Exception:
    print('Tratamento generico')

print('Não parei a execucao') 