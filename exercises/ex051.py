print("="*25)
print("   10 TERMOS DE UMA PA   ")
print("="*25)

a1 = int(input("informe o primeiro termo: "))
r = int(input("Informe a razao: "))
n = a1 + (10 - 1) * r
count = 0

for i in range(a1, n + 1, r):
    print(i, end=' -> ')
    count += 1
print("Acabou")