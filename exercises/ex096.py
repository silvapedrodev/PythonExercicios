def area(b, h):
    a = b * h
    print(f'A área de um terreno {b}x{h} é de {a}m².')


print(' Controle de Terrenos ')
print('-' * 22)
b = float(input('LARGURA (m): '))
h = float(input('COMPRIMENTO (m): '))

area(b, h)
