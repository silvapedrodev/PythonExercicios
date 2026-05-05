values = []

for i in range(0, 5):
    num = int(input("Digite um valor: "))
    if not values or num > values[-1]:
        values.append(num)
        print(f"Adicionado na posição ao final da lista")
    else:
        pos = 0
        while pos < len(values) and values[pos] < num:
            pos += 1
        values.insert(pos, num)
        print(f"Adicionado na posição {pos} da lista")

print("=-" * 20)
print(f"saiu, {values}")
