def half(value=0, formato=False):
    value /= 2
    return value if not formato else moeda(value)


def double(value=0, formato=False):
    value *= 2
    return value if not formato else moeda(value)


def increase(value=0, taxa=0, formato=False):
    res = value + (value * taxa / 100)
    return res if not formato else moeda(res)


def decrease(value=0, taxa=0, formato=False):
    res = value - (value * taxa / 100)
    return res if not formato else moeda(res)


def moeda(value=0, currency="R$"):
    return f"{currency}{value:.2f}".replace(".", ",")


def resumo(value, tax, tax_2):
    print("-" * 32)
    print("RESUMO DO VALOR".center(35))
    print("-" * 32)
    print(f"Valor analisado: \t{moeda(value)}")
    print(f"Dobro do preço: \t{double(value, True)}")
    print(f"Metade do preço: \t{half(value, True)}")
    print(f"{tax}% de aumento: \t{increase(value, tax, True)}")
    print(f"{tax_2}% de redução: \t{decrease(value, tax_2, True)}")
    print("-" * 32)
