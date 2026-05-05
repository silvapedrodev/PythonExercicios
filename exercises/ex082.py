values = []
odd = []
even = []

while True:
    values.append(int(input("Digite um número: ")))

    op = str(input("Quer continuar? [S/N] ")).strip().upper()
    if op == "N": break

for i, v in enumerate(values):
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)

print("=" * 25)
print(f"A lista completa é: {values}")
print(f"A lista de pares é: {even}")
print(f"A lista de ímpares é: {odd}")
