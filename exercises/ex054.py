from datetime import date

currentYear = date.today().year
countMaior = 0
countMenor = 0

for i in range(1, 8):
    nasc = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    idade = currentYear - nasc
    if (idade >= 21):
        countMaior += 1
    else:
        countMenor += 1

print(f"ao todo tivemos {countMaior} pessoas maiores de idade (21 anos)")
print(f"E também {countMenor} pessoas menores de idade (21 anos)")