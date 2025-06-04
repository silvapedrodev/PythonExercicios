# Usando lista
listPeso = []
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    listPeso += [peso]

print(f"O maior peso lido foi {max(listPeso)}Kg")
print(f"O menor peso lido foi {min(listPeso)}Kg:")

# Usando variaveis

"""
maiorPeso = 0
menorPeso = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))

    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print(f"O maior peso lido foi {maiorPeso:.1f}Kg")
print(f"O menor peso lido foi {menorPeso:.1f}Kg:") """