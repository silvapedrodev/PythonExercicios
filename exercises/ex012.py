preco = float(input('Qual é o preço do produto? R$'))
novoPreco = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco:.2f}, na promoção com deconto de 5% vai custar R${novoPreco:.2f}')
