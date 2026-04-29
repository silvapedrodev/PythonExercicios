num = 0
soma = 0
tot = 0

while num != 999:
    num = int(input("Digite um número [999 pra parar]: "))
    if num != 999:
        soma += num
        tot += 1
print(f"Você digitou {tot} números e a soma entre eles foi {soma}")