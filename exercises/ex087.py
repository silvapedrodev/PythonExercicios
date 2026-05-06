matrices = [[], [], []]
sum_even_values = 0
sum_third_column = 0

for i in range(0, 3):
    for j in range(0, 3):
        matrices[i].append(int(input(f"Digite um valor para [{i},{j}]: ")))
        sum_even_values += matrices[i][j] if matrices[i][j] % 2 == 0 else 0
        sum_third_column += matrices[i][j] if j == 2 else 0

print("-=" * 25)
for matrix in matrices:
    for value in matrix:
        print(f"[{value:^5}]", end="")
    print()

print("-=" * 25)
print(f"A soma dos valores pares é: {sum_even_values}")
print(f"A soma dos valores da terceira coluna é: {sum_third_column}.")
print(f"O maior valor da segunda linha é: {max(matrices[1])}.")
