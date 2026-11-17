from ex107.moeda import increase, double, half

value = float(input("Digite um preço: R$"))
print(f"A metade de R${value} é R${half(value)}")
print(f"O dobro de R${value} é R${double(value)}")
print(f"Aumentando 10%, temos R${increase(value, 10)}")
