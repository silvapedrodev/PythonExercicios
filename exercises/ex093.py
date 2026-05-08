player = dict()
goals = []

player['nome'] = str(input("Nome do jogador: "))
for i in range(1, int(input(f"Quantas partidas {player['nome']} jogou? ")) + 1):
    goals.append(int(input(f"  Quantos gols na partida {i}: ")))
player['gols'] = goals
player['total'] = sum(player['gols'])

print("-=" * 25)
print(player)
print("-=" * 25)
for key, value in player.items():
    print(f"O campo {key} tem o valor {value}")
print("-=" * 25)
print(f"O jogador {player['nome']} jogou {len(player['gols'])} partidas.")
for i, v in enumerate(player['gols']):
    print(f"   => Na partida {i + 1}, fez {v} gols.")
print(f"Foi um total de {player['total']} gols")
