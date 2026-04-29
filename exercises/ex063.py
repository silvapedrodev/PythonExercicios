print("-" * 25)
print("Sequência de Fibonacci")
print("-" * 25)

f = int(input("Quantos termos você quer mostrar? "))

i = 0
a = 0
b = 1

while i < f:
    print(f'{a}', end=' -> ')
    proximo = a + b
    a = b
    b = proximo
    i += 1
print("FIM")