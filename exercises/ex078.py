values = []

for i in range(0, 5):
    num = int(input(f"Digite um valor para a Posição {i}: "))
    values.append(num)

maior = max(values)
menor = min(values)

pos_maior = []
pos_menor = []

for i, v in enumerate(values):
    if v == maior:
        pos_maior.append(i)

    if v == menor:
        pos_menor.append(i)

print("-" * 30)
print(f"Você digitou os valores {values}")
print(f"O maior valor digitado foi {maior} {'na posição' if len(pos_maior) == 1 else 'nas posições'}", *pos_maior)
print(f"O menor valor digitado foi {menor} {'na posição' if len(pos_menor) == 1 else 'nas posições'}", *pos_menor)
