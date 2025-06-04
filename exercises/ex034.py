salario = float(input('Qual o salário do funcionário? R$'))

if salario > 1250:
    ajuste = salario + (salario * 10 / 100)
else:
    ajuste = salario + (salario * 15 / 100)

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${ajuste:.2f} agora.')
