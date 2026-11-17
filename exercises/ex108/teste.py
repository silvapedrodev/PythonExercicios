from ex108.moeda import increase, double, half, moeda

value = float(input("Digite um preço: R$"))
print(f"A metade de {moeda(value)} é {moeda(half(value))}")
print(f"O dobro de {moeda(value)} é {moeda(double(value))}")
print(f"Aumentando 10%, temos {moeda(increase(value, 10))}")
