from ex109.moeda import increase, double, half, moeda

value = float(input("Digite um preço: R$"))
print(f"A metade de {moeda(value)} é {half(value, True)}")
print(f"O dobro de {moeda(value)} é {double(value, True)}")
print(f"Aumentando 10%, temos {increase(value, 10, True)}")
