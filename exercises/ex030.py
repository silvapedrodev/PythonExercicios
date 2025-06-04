num = int(input('Me diga um numero qualquer: '))

if num % 2 == 0:
    print(f'O número {num} é \033[1;94mPAR\033[0m')
else:
    print(f'O número {num} é \033[1;94mIMPAR\033[0m')