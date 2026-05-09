players = []

while True:
    player = {}
    goals = []

    player['nome'] = str(input("Nome do jogador: "))
    matches = int(input(f"Quantas partidas {player['nome']} jogou? "))

    for i in range(matches):
        goals.append(int(input(f"  Quantos gols na partida {i + 1}: ")))

    player['gols'] = goals.copy()
    player['total'] = sum(player['gols'])

    players.append(player.copy())

    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'SN': break
        print("Erro! Responda S ou N.")

    if op == 'N': break

players.sort(key=lambda player: player['total'], reverse=True)

print("-=" * 25)
print("Cod ", end='')
for i in player.keys():
    print(f"{i:<15}", end='')
print()
print("-" * 45)
for key, v in enumerate(players):
    print(f'{key:>3} ', end='')
    for p in v.values():
        print(f"{str(p):<15}", end='')
    print()
print("-" * 45)

while True:
    op_player = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if op_player == 999: break

    if 0 <= op_player < len(players):
        print(f" -- LEVANTAMENTO DO JOGADOR {players[op_player]['nome']}:")
        for i, v in enumerate(players[op_player]['gols']):
            print(f"  No jogo {i + 1} fez {v} {'gol' if v == 1 else 'gols'}.")
    else:
        print(f"ERRO! Não existe jogador com código {op_player}!")
    print('-' * 45)
print("<< VOLTE SEMPRE >>")
