import builtins

from time import sleep


def title(cor, text):
    print(f"\033[{cor}m\033[97m")
    print("~" * (len(text) + 4))
    print(f"  {text}")
    print("~" * (len(text) + 4))
    print("\033[0m")
    sleep(1)


def help_system():
    while True:
        title("48;5;106", "SISTEMA DE AJUDA PyHELP")

        res = input("Função ou biblioteca > ").strip().lower()
        if res == 'fim':
            title("41", "ATÉ LOGO!")
            return

        if hasattr(builtins, res):
            title("44", f"Acessando o comando '{res}'")
            print("\033[107m\033[30m", end="")
            help(getattr(builtins, res))
            print("\033[0m", end="")
            sleep(2)
        else:
            print("Função ou biblioteca não encontrada!")


help_system()
