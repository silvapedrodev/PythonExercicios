brasileirao_2026 = (
    "Palmeiras", "Flamengo", "Fluminense", "São Paulo", "Athletico-PR",
    "Bahia", "Red Bull Bragantino", "Coritiba", "Vitória", "Botafogo",
    "Atlético-MG", "Internacional", "Vasco da Gama", "Grêmio", "Cruzeiro",
    "Santos", "Corinthians", "Mirassol", "Remo", "Chapecoense"
)

print("-=" * 20)
print(f"Lista de times do Brasileirão {brasileirao_2026}")
print("-=" * 20)
print(f"Os 5 primeiros são {brasileirao_2026[0:5]}")
print("-=" * 20)
print(f"Os 4 últimos são {brasileirao_2026[-4:]}")
print("-=" * 20)
print(f"Os time em ordem alfabética {sorted(brasileirao_2026)}")
print("-=" * 20)
print(f"A Chapecoense está ná {brasileirao_2026.index("Chapecoense") + 1}º posição")
