num = int(input('Digite um numero: '))
print(f'Analisando o número {num}...')

u = num % 10
dez = (num // 10) % 10
cent = (num // 100) % 10
mi = num // 1000

print(f'Unidade: {u}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {mi}')
