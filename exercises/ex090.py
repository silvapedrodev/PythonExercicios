student = dict()

student['nome'] = str(input("Nome: "))
student['média'] = float(input(f"Media de {student['nome']}: "))

if student['média'] >= 7:
    student['situação'] = "Aprovado"
elif 5 <= student['média'] < 7:
    student['situação'] = "Recuperação"
else:
    student['situação'] = "Reprovado"

print("=-" * 20)
for k, v in student.items():
    print(f"  - {k} é igual a {v}")
