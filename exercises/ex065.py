soma = 0
quant = 0
media = 0
menor = 0
maior = 0

while True:
    num = int(input("Digite um número: "))

    if quant == 0:
        menor = maior = num
    else:
        if num < menor: menor = num
        if num > maior: maior = num

    soma += num
    quant += 1

    op = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if op == "N": break

media = soma / quant
print(f"Você digitou {quant} {'número' if quant == 1 else 'números'} e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
