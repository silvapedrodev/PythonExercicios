expression = str(input("Digite a expressão: "))

count = 0
valid = True

for c in expression:
    if c == "(":
        count += 1
    elif c == ")":
        count -= 1

    if count < 0:
        valid = False
        break

if count != 0:
    valid = False

print(f"Sua expressão está {'válida!' if valid else 'errada!'}")
