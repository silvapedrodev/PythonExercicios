# Exercício sugerido pelo Professor Guanabara na aula 13 de exercícios.

produto = float(input('Qual o preço do produto? R$'))
pix = produto - (produto * 10/100)
parcelado = produto + (produto * 8/100)

print(f'\nPagamento no PIX terá 10% de descosto e parcelado 8% de juros.')
print(f'Seu produto de R${produto:.2f}, ficará R${pix:.2f} no PIX ou R${parcelado:.2f}.')
