medida = float(input('Digite uma distância em metros: '))
print(f'A medida de {medida}m correspode a: '
      f'\n{medida/1000}km '
      f'\n{medida/100}hm '
      f'\n{medida/10}dam '
      f'\n{medida*10:.0f}dm '
      f'\n{medida*100:.0f}cm '
      f'\n{medida*1000:.0f}mm')
