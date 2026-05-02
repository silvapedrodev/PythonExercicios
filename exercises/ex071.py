print("=" * 26)
print(f"{'BANCO':^26}")
print("=" * 26)

withdraw_amount = int(input("Qual valor voce quer sacar? "))

for bill in [50, 20, 10, 1]:
    count = 0

    while withdraw_amount >= bill:
        withdraw_amount -= bill
        count += 1

    if count > 0:
        print(f"Total de {count} cédulas de R$ {bill}")
print("=" * 26)
print("Volte sempre ao BANCO! Tenha um bom dia!")

''''
# Sem usar while, somente com for
for bill in [50, 20, 10, 1]:
    count = withdraw_amount // bill
    withdraw_amount %= bill
    if count > 0:
        print(f"Total de {count} cédulas de R$ {bill}")
'''
