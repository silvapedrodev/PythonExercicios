from time import sleep


def line():
    print("-=" * 20)


def count(i, j, k):
    if k == 0:
        k = 1

    k = -abs(k) if i > j else abs(k)
    j += 1 if k > 0 else -1

    for n in range(i, j, k):
        print(n, end=' ')
    sleep(0.3)

    print('FIM!')


def main():
    line()
    print("Contagem de 1 até 10 de 1 em 1")
    count(1, 10, 1)

    line()
    print("Contagem de 10 até 0 de 2 em 2")
    count(10, 0, 2)

    line()
    print("Personalize sua contagem!")

    i = int(input("Início: "))
    j = int(input("Fim: "))
    k = int(input("Passo: "))

    line()

    if k == 0:
        k = 1

    print(f"Contagem de {i} até {j} de {abs(k)} em {abs(k)}")
    count(i, j, k)


main()
