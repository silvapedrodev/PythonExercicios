from random import randint
from time import sleep
num = randint(1, 5)
print('\033[34m-=-\033[0m'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('\033[34m-=-\033[0m'*20)
res = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)


if res == num:
    print('PARABÉNS! Você csonseguiu me vencer!')
else:
    print(f'Eu ganhei pensei no número {num} e não no {res}!')
