num = int(input("Digite um numero: "))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(i, end=" ")

print(f"\n\33[mO numero {num} foi divisível {tot} vezes")
if tot == 2:
    print("E por isso ele É PRIMO")
else:
    print("E por isso ele NÃO É PRIMO")