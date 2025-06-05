oldManAge = 0
oldManName = ''
youngerWoman = 0
media = 0

for i in range(1, 5):
    print(f"----- {i}º PESSOA -----")
    pessoa = {}
    name = input("Nome: ").strip().capitalize()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper()

    media += idade

    if i == 1 and sexo == "M":
        oldManName = name
        oldManAge = idade
    if sexo == "M" and idade > oldManAge:
        oldManName = name
        oldManAge = idade
    if sexo == "F" and idade < 20:
        youngerWoman += 1


media = media / 4
print(f"A media de idade do grupo é de {media:.1f} anos")
print(f"O homem mais velho tem {oldManAge} e se chama {oldManName}")
print(f"Ao todo são {youngerWoman} {'mulher' if youngerWoman == 1 else 'mulheres'} com menos de 20 anos")