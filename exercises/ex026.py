frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeila letra A aparece na posição {frase.find('A')+1}')
print(f'A Ultima letra A aparece na posição {frase.rfind('A')+1}')
