from time import sleep

from ex115.lib.arquivo import *
from ex115.lib.interface import *

file = "people.txt"

if not file_exists(file): create_file(file)

while True:
    res = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair'])

    match res:
        case 1:
            read_file(file)
        case 2:
            header("NOVO CADASTRO")
            name = str(input("Nome: ")).strip()
            age = read_int("idade: ")
            register(file, name, age)
        case 3 | 0:
            header("Saindo do sistema... Até logo!")
            break
        case _:
            print(f'\033[91mERRO! Digite uma opção válida.\033[0m')
    sleep(1)
