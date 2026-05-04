import random

numbers = tuple(random.choices(range(1, 11), k=5))

print("Os valores sorteados foram:", *numbers)
print(f"O maior valor sorteado foi {max(numbers)}")
print(f"O menor valor sorteado foi {min(numbers)}")
