values = []

while True:
    num = int(input("Digite um valor: "))

    if num not in values:
        values.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")

    op = input("Quer continuar? [S/N] ").strip().upper()
    if op == "N": break

values.sort()
print("-=" * 30)
print(f"Você digitou os valores: {values}")
