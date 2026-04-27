num_1 = int(input(("Primeiro valor: ")))
num_2 = int(input(("Segundo valor: ")))

while True:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')

    op = int(input(">>>> Qual é sua opção? "))

    match op:
        case 1:
            print(f"A soma entre {num_1}+{num_2} é: {num_1 + num_2}")
        case 2:
            print(f"O resultado de {num_1}x{num_2} é: {num_1 * num_2}")
        case 3:
            maior = max(num_1, num_2)
            print(f"Entre {num_1} e {num_2} o maior valor é: {maior}")
        case 4:
            print("Informe os números novamente: ")
            num_1 = int(input(("Primeiro valor: ")))
            num_2 = int(input(("Segundo valor: ")))
        case 5:
            print("Finalizando...")
            print("=-" * 11)
            print("Fim do programa! Volte sempre!")
            break
        case _:
            print("Opção inválida. Tente novamente")

    print("=-" * 10)
