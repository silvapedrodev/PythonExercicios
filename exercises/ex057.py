sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while sexo not in ["M", "F"]:
    sexo = str(input("Dados inválidos. Por Favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso")
