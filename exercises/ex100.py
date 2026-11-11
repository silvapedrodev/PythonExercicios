from random import randint
from time import sleep


def generate_num(values):
    print(f'Sorteando 5 valores da lista: ', end="")
    for i in range(0, 5):
        n = randint(1, 10)
        sleep(0.3)
        values.append(n)
        print(n, end=" ")
    print("PRONTO!")


def sum_even_number(values):
    sum = 0
    for value in values:
        if value % 2 == 0:
            sum += value
    print(f"Somando os valores pares de {values}, temos {sum}")


values = []
generate_num(values)
sum_even_number(values)
