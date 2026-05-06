people = []
person = []

while True:
    person.append(str(input("Nome: ")))
    person.append(float(input("Peso: ")))

    people.append(person[:])
    person.clear()

    op = str(input("Quer continuar? [S/N] ")).strip().upper()
    if op == "N": break

max_weight = max(p[1] for p in people)
min_weight = min(p[1] for p in people)

heaviest = [f'[{p[0]}]' for p in people if p[1] == max_weight]
lightest = [f'[{p[0]}]' for p in people if p[1] == min_weight]

print("-=" * 25)
print(f"Ao todo você cadastrou {len(people)} pessoas.")
print(f"O maior peso foi de {max_weight}kg. Peso de {''.join(heaviest)}")
print(f"O menor peso foi de {min_weight}kg. Peso de {''.join(lightest)}")
