soma = 0
count = 0

for i in range(1, 7):
    num = int(input(f"digite o {i}º valor: "))
    if num % 2 == 0:
        soma += num
        count += 1

print(f"Você informou {count} PARES e a soma foi {soma}")