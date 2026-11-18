def read_money(value):
    while True:
        num = str(input(value).strip().replace(",", "."))

        if (num == '' or num.isalpha()):
            print(f'\033[91mERRO: "{num}" é um preço inválido!\033[0m')
            continue

        return float(num)
