print("="*25)
print("   10 TERMOS DE UMA PA   ")
print("="*25)

a1 = int(input("informe o primeiro termo: "))
r = int(input("Informe a razao da PA: "))

termo = a1
i = 0
an = 0
plus= 10

while plus != 0:
    an += plus
    while i < an:
        print(termo, end=' -> ')
        termo += r
        i += 1
    print("Pausa")
    plus = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {an} termos mostrados.")