print(f'{' LOJAS ALVINEGRO ':=^40}')
preco = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheito/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')

option = int(input('Qual é sua opção? '))

if option == 1:
    total = preco - (preco * 10 / 100)
elif option == 2:
    total = preco - (preco * 5 / 100)
elif option == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif option == 4:
    total = preco + (preco * 20 / 100)
    totParc = int(input('Quantas parcelas? '))
    parcela = total / totParc
    print(f'Sua compra será parcelada em {totParc}x de {parcela:.2f} COM JUROS.')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
