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
