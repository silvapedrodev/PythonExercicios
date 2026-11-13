def ficha(gols, name="<desconhecido>"):
    print("-" * 20)
    return f"O jogador {name} fez {gols} {'gol' if gols == 1 else 'gols'} no campeonato."


name = str(input("Nome do jogador: ")).strip()
gols = str(input("Número de gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if name == '':
    print(ficha(gols))
else:
    print(ficha(gols, name))
