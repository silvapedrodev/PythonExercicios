matrices = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f"Digite um valor para [{i},{j}]: "))
        matrices[i].append(num)

print("-" * 30)
for matrix in matrices:
    for value in matrix:
        print(f"[{value:^5}]", end="")
    print()
