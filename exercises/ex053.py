frase = str(input("Digite uma frase: ")).strip().upper()
words = frase.split()
frase_unida = ''.join(words)
frase_inversa =''

#frase_inversa = frase_unida[::-1] # Opeção com fatiamento

for i in range(len(frase_unida) - 1, -1, -1):
    frase_inversa += frase_unida[i]

print(f"O Inverso de {frase_unida}, {frase_inversa}")

if frase_unida == frase_inversa:
 print("É um palíndromo")
else:
 print("NÃO é um palíndromo")