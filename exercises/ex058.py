from random import randint

num = randint(0, 10)

print("Sou seu computador... \nAcabei de pensar em um número de 0 a 10.")
print("Será que você consegue adivinhar qual foi?")

palpite = -1
cont = 0

while palpite != num:
    palpite = int(input("Qual seu palpite? "))
    cont += 1

    if palpite == num:
        break

    if palpite < num:
        print("Mais... tente mais uma vez.")
    else:
        print("Menos... tente mais uma vez.")

print(f"Acertou com {cont} tentativa. Parabéns!")
