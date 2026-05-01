from random import randint

print("-=" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=" * 15)

v = 0
while True:
    while True:
        op = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]

        if op in ('P', 'I'):
            break
        print("Opção inválida. Tente novamente.")

    num = int(input("Digite um número: "))
    pc = randint(0, 10)
    total = num + pc

    print("-=" * 15)
    print(f"Você jogou {num} e o computador {pc}. Total de {total} ", end='')
    print(f"DEU {'PAR' if total % 2 == 0 else 'ÍMPAR'}")
    print("-=" * 15)

    win = (op == "P" and total % 2 == 0) or (op == "I" and total % 2 == 1)

    if win:
        print("Você VENCEU! Vamos jogar novamente...")
        print("-=" * 15)
        v += 1
    else:
        print("VOCÊ PERDEU!")
        print("-=" * 15)
        break

print(f"GAME OVER! Você venceu {v} {'vez' if v == 1 else 'vezes'}")
