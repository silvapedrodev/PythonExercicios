values = [[], []]

for i in range(1, 8):
    num = int(input(f"Digite o {i}º valor: "))

    if num % 2 == 0:
        values[0].append(num)
    else:
        values[1].append(num)

for v in values:
    v.sort()

print("-=" * 30)
print(f"Os valores pares digitados foram: {values[0]}")
print(f"Os valores ímpares digitados foram: {values[1]}")
