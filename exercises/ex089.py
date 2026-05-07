students = []

while True:
    name = str(input("Nome: "))
    grade_1 = float(input(f"Nota 1: "))
    grade_2 = float(input(f"Nota 2: "))
    avg = (grade_1 + grade_2) / 2
    students.append([name, [grade_1, grade_2], avg])

    op = str(input("Quer continuar? [S/N] ")).strip().upper()
    if op == "N": break

print("=-" * 30)
print(f"{'No.':<5}{'NOME':<12}{'MEDIA':>5}")
print("-" * 25)
for i, student in enumerate(students):
    print(f"{i:<5}{student[0]:<12}{student[2]:>6.1f}")
print("-" * 25)

while True:
    op_grade = int(input("Mostrar notas de qual aluno? (999 para interromper): "))
    if op_grade == 999:
        print("Finalizando...")
        break

    if op_grade < 0 or op_grade >= len(students):
        print("Aluno inválido!")
        continue

    name = students[op_grade][0]
    grades = students[op_grade][1]

    print(f"As notas de {name} são {grades}")
print("<<< VOLTE SEMPRE >>>")
