def fatorial(n, show=False):
    """
        -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """

    print("--" * 20)
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
        if show: print(f"{i} x", end=" ")
    return (f"{'= ' if show else ''}{fat}")


print(fatorial(5, True))
