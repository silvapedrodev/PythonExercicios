soma = 0
count = 0

while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999: break

    soma += num
    count += 1
print(f"A soma dos {count} valores foi {soma}!")
