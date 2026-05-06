from random import  sample
from time import sleep

print("-" * 30)
print(f"{'JOGUE NA MEGA SENA':^30}")
print("-" * 30)

num_games = int(input("Quantos números você quer jogar? "))

print(f"{' SORTEIO ':-^30}")
for i in range(1, num_games + 1):
    draw = sample(range(1, 61), 6)
    draw.sort()

    sleep(1)
    print(f"Jogo {i}: {draw}")

print(f"{' < BOA SORTE > ':-^30}")
