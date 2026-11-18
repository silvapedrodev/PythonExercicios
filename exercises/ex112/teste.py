from ex112.utils import moeda, dado

value = dado.read_money("Digite um preço: R$")
moeda.resumo(value, 20, 12)
