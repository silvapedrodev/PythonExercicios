def leiaInt(value):
    print('-' * 20)
    while True:
        num = input(value).strip()

        if num.isnumeric(): return int(num)
        print("\033[91mERRO! Digite um número válido.\033[0m")


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
