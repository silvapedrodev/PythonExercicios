from operator import itemgetter
from random import randint
from time import sleep

game = {}

for i in range(1, 5):
    game[f'jogador{i}'] = randint(1, 6)

for k, v in game.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.8)

print(f"-=" * 25)

raking = sorted(game.items(), key=itemgetter(1), reverse=True)
print("  == RANKING DOS JOGADORES ==")
for i, v in enumerate(raking):
    print(f'  {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.8)
