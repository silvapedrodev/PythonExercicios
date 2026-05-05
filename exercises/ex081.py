values = []

while True:
    num = int(input("Digite um valor: "))
    values.append(num)

    op = str(input("Quer continuar? [S/N]: ").strip().upper())
    if op == "N": break

print("=" * 25)
print(f"Você digitou {len(values)} elementos")
values.sort(reverse=True)
print(f"Os valores em ordem decrescente são {values}")
if 5 in values:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
