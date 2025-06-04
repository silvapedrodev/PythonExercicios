speed = float(input('Qual é a velocidade atual do carro? '))

if speed > 80:
    multa = (speed - 80) * 7
    print('MULTADO! Você excedeu p limite perimitido que é de 80Km/h')
    print(f'Você deve pagar um multa de R${multa:.2f}')

print('Tenha um bom dia! Dirija com segurança!')
