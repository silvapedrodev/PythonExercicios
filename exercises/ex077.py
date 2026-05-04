words = ("aprender", "programar", "linguagem", "python", "curso",
         "gratis", "estudar", "praticar", "trabalhar", "mercado",
         "programador", "futuro", "corinthians")

for w in words:
    print(f"\nNa palavra {w.upper()} temos ", end="")

    for letter in w:
        if letter.lower() in "aeiou":
         print(letter, end="")

