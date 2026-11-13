def vote(birth_year):
    from datetime import date

    current_year = date.today().year
    age = current_year - birth_year

    print(f"Com {age} anos: ", end="")
    if (18 <= age <= 60):
        return f"VOTO OBRIGATÓRIO."
    elif (age >= 60):
        return f"VOTO OPCIONAL."
    else:
        return f"VOTO NEGADO."


print("-=" * 20)
birth_year = int(input("Em que ano você nasceu? "))
print(vote(birth_year))
