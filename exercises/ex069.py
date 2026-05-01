maior_idade = 0
men = 0
women = 0

while True:
    print("-" * 25)
    print("   CADASTRE UMA PESSOA   ")
    print("-" * 25)

    idade = int(input("Idade: "))
    while True:
        sexo = str(input("Sexo: [M/F]: ")).strip().upper()
        if sexo and sexo[0] in ("M", "F"):
            sexo = sexo[0]
            break
        print("Sexo inválido. Tente novamente.")

    if idade >= 18:
        maior_idade += 1

    if sexo == "M":
        men += 1

    if sexo == "F" and idade < 20:
        women += 1

    print("-" * 25)
    while True:
        stop = str(input("Quer continuar [S/N] ")).strip().upper()
        if stop and stop[0] in ("S", "N"):
            stop = stop[0]
            break
        print("Opção inválida.")

    if stop == "N":
        break

print("-=" * 15)
print(f"Total de pessoas com mais de 18: {maior_idade}")
print(f"Ao todo temos {men} {'homem cadastrado' if men == 1 else 'homens cadastrados'}")
print(f"E temos {women} {'mulher' if women == 1 else 'mulheres'} com menos de 20 anos")
