def half(value=0):
    value /= 2
    return value


def double(value=0):
    value *= 2
    return value


def increase(value=0, taxa=0):
    res = value + (value * taxa / 100)
    return res


def decrease(value=0, taxa=0):
    res = value - (value * taxa / 100)
    return res


def moeda(value=0, currency="R$"):
    return f"{currency}{value:.2f}".replace(".", ",")
