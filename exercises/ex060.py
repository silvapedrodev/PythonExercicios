num = int(input("Digite um número para \ncalcular seu Fatorial: "))
count = num
fator = 1

print(f"Calculando {num}!", end=' = ')
while count > 0:
    fator *= count
    print(f"{count}{' x ' if count > 1 else ' = '}", end='')
    count -= 1
print(fator)

# --- Usando for ---
'''
for i in range(num, 0, -1):
    fator *= i
    print(f"{i}{' x ' if i > 1 else ' = '}", end='')
print(fator)
'''