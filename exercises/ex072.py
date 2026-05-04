numbers_in_full = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

while True:
    num = int(input("Digite um número entre 0 e 20: "))

    if 0 <= num <= 20:
        print(f"você digitou o numero {numbers_in_full[num]}")
        op = str(input("Quer continuar [S/N]? ")).strip().upper()
        if op == "S":
            continue
        break
    print("Tente novamente. ", end="")
