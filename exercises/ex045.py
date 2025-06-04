from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

player = int(input('Qual é sua jogada? '))
if player != 0 and player != 1 and player != 2:
    print('JOGADA INVÁLIDA')
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    print('-=' * 12)
    print(f'Computador jogou {itens[pc]}')
    print(f'Jogador jogou {itens[player]}')
    print('-=' * 12)

if pc == player:
    print('EMPATE')
elif pc == 0:
    if player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
elif pc == 1:
    if player == 0:
        print('COMPUTADOR VENCE')
    elif player == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:
    if player == 0:
        print('JOGADOR VENCE')
    elif player == 1:
        print('COMPUTADOR VENCE')
