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


def read_float(value):
    while True:
        try:
            n = float(input(value))
            return n
        except ValueError:
            print(f'\033[91mERRO: por favor, digite um número real válido.\033[0m')
        except (KeyboardInterrupt):
            print("\033[91mUsuário preferiu não digitar esse número.\033[0m")
            return 0


i = read_int("Digite um valor inteiro: ")
f = read_float("Digite um valor real: ")
print(f"O valor inteiro digitado foi {i} eo real foi {f}")
