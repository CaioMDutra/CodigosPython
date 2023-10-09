import random

lista = ['Kylle', 'And', 'flz', 'allan', 'dk', 'Perera', 'fer', 'gbrl', 'feep', 'bunny']

while True:
    quantidade_nomes = input('Quantos nomes deseja sortear? ')
    if quantidade_nomes.isdigit():
        quantidade_nomes = int(quantidade_nomes)
        if quantidade_nomes < len(lista):
            break
        else:
            print(f'Quantidade inválida, a lista tem {len(lista)} quantidade_nomes.')
    else:
        print(f'{quantidade_nomes} não é um número válido.')

quantidade_nomes = random.sample(lista, quantidade_nomes)
print(f'Time 1: {quantidade_nomes}')

lista = [nome for nome in lista if nome not in quantidade_nomes]

print(f'Time 2: {lista}')

