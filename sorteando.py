import random

num = range(1,10+1)

maquina = random.choice(num)

while True:
    sorte = input('Escolha um numero de 1 a 10 ')
    if  sorte.isdigit():
        sorte == maquina
        break
    if maquina == sorte:        
        print(f'Você acertou o numero escolhido era {maquina}'),
        
    else:            
        print('Vc errou!!!')

print(f'Vc acertou o numero escolhido foi {maquina}')
 
'''val = len(num)

while True:
    num = list(map(int, num))
    sorte = input('Escolha um numero de 1 a 10')
    if sorte.isdigit() and sorte == maquina:        
        break
    if sorte.isdigit() and sorte > val:
        print('Numero invalido digite um numero entre 1 e 10')
    else:
        print('Digite um numero valido')

print(f'O numero sorteado foi {maquina}')'''
    
    