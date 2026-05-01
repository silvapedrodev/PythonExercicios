print("-" * 30)
print("     LOJA SUPER BARATÃO")
print("-" * 30)

soma = 0
count_over_1000 = 0
cheaper = {'name': '', 'price': float('inf')}

while True:
    product = str(input("Nome do produto: "))
    price = float(input("Preço R$"))

    soma += price

    if price >= 1000:
        count_over_1000 += 1

    if price <= cheaper['price']:
        cheaper['name'] = product
        cheaper['price'] = price

    while True:
        res = str(input("Quer continuar? [S/N]")).strip().upper()
        if res and res[0] in ("S", "N"):
            res = res[0]
            break
        print("Opção inválida.")

    if res == "N": break

print("------- FIM DO PROGRAMA -------")
print(f"O total de compra foi R${soma:.2f}")
print(f"Temos {count_over_1000} {'produto'
if count_over_1000 == 1 else
'produtos'} custando mais de R$1000.00")
print(f"O produto mais barato foi {cheaper['name']} que custa R${cheaper['price']:.2f}")
