from datetime import date
anoAtual = date.today().year

nasc = int(input('Ano de nacimento: '))
idade = anoAtual - nasc
classif = ''
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    classif = 'MIRIM'
elif idade <= 14:
    classif = 'INFANTIL'
elif idade <= 19:
    classif = 'JUNIOR'
elif idade <= 25:
    classif = 'SENIOR'
else:
    classif = 'MASTER'

print(f'Classificação: {classif}')
