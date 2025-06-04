from datetime import date

nasc = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {anoAtual}.')

if idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    ano = anoAtual + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
else:
    saldo = idade - 18
    ano = anoAtual - saldo
    print(f'Você ja deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}.')
