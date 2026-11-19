def read_int(value):
    while True:
        try:
            n = int(input(value))
            return n
        except ValueError:
            print(f'\033[91mERRO: por favor, digite um número inteiro válido.\033[0m')
        except (KeyboardInterrupt):
            print("\033[91mUsuário preferiu não digitar esse número.\033[0m")
            return 0


def line(size=40):
    return "-" * size


def header(text):
    print(line())
    print(text.center(40))
    print(line())


def menu(list):
    header("MENU PRINCIPAL")
    for index, item in enumerate(list, start=1):
        print(f"\033[33m{index}\033[m- \033[34m{item}\033[m")
    print(line())
    op = read_int("\033[32mSua opção: \033[m")
    return op
