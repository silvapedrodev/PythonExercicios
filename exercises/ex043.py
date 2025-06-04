weight = float(input('Qual é seu peso? (KG) '))
height = float(input('Qual é sua altura? (cm) '))

imc = weight / ((height / 100) ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc < 30:
    print('Você está em SOBREPESO')
elif imc < 40:
    print('Você está em OBESIDADE')
elif imc < 50000:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
else:
    print('Você é um OBJETO SUPERMASSIVO.')
    print('A matéria ao seu redor corre risco de colapsar sob sua massa formando um buraco negro.')