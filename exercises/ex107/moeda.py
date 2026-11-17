def half(value):
    value /= 2
    return value


def double(value):
    value *= 2
    return value


def increase(value, taxa):
    res = value + (value * taxa / 100)
    return res


def decrease(value, taxa):
    res = value - (value * taxa / 100)
    return res
