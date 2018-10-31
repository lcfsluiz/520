ling = input("qual a melhor linguagem de programação ?")
ling = ling.strip().lower()

if ling == 'python':
    print('Você está no caminho certo')
elif ling == 'html' or ling == 'css':
    raise ValueError('isso não é linguagem de programação')
else:
    print('Mude para python!') 

except ValueError as e:
    print(e) 
    