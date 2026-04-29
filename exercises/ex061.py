print("="*25)
print("   10 TERMOS DE UMA PA   ")
print("="*25)

a1 = int(input("informe o primeiro termo: "))
r = int(input("Informe a razao: "))

termo = a1
i = 0

while i < 10:
    print(termo, end=' -> ')
    termo += r
    i += 1
print("FIM")