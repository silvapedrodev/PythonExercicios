values = []

for i in range(0, 4):
    num = int(input(f"Digite o {i + 1}º valor: "))
    values.append(num)

values_tuple = tuple(values)
even_numbers = tuple(n for n in values_tuple if n % 2 == 0)

print(f"Você digitou os valores: {values_tuple}")
print(f"O valor 9 apareceu {values_tuple.count(9)} vezes")
if 3 in values_tuple:
    print(f"O valor 3 apareceu na {values_tuple.index(3) + 1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("Os valores pares digitados foram:", *even_numbers)
