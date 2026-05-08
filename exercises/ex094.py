people = []
person = dict()
soma = 0

while True:
    person.clear()
    person['nome'] = str(input("Nome: "))

    while True:
        person['sexo'] = str(input("Sexo [M/F]: ")).strip().upper()
        if person['sexo'] in 'MF': break
        print("ERRO! Por favor, digite somente M ou F.")

    person['idade'] = int(input("Idade: "))
    soma += person['idade']

    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op in 'SN': break
        print("Erro! Responda S ou N.")
    people.append(person.copy())
    if op == 'N': break

media = soma / len(people)

print("-=" * 25)
print(f"A) Ao todo temos {len(people)} pessoas cadastradas.")
print(f"B) A média de idade é de {media:5.2f} anos.")
print("C) As mulheres cadastradas foram ", end='')
for p in people:
    if p['sexo'] == 'F':
        print(f"{p['nome']}", end=', ')
print()

print(f"D) Lista das pessoas que estão acima da média: ")
for k, v in enumerate(people):
    if v['idade'] >= media:
        print(f"{'nome':>10} = {v['nome']};", end=' ')
        print(f"sexo = {v['sexo']};", end=' ')
        print(f"idade = {v['idade']};")
print("<< ENCERRADO >>")
