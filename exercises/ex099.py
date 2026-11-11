from time import sleep


def maior(*num):
    greatest = None

    print("-=" * 24)
    print("Analisando os valores passados...")
    for i in num:
        if (greatest is None or i > greatest): greatest = i
        sleep(0.3)
        print(i, end=" ")
    if greatest is None: greatest = 0
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {greatest}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
