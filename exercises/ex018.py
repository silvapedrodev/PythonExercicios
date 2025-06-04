from math import radians, sin, cos, tan

angle = float(input('Digite o ângulo que você deseja: '))
rad = radians(angle)

print(f'O ângulo de {angle:.2f} tem o SENO de {sin(rad):.2f}')
print(f'O ângulo de {angle:.2f} tem o COSSENO de {cos(rad):.2f}')
print(f'O ângulo de {angle:.2f} tem o TANGENTE de {tan(rad):.2f}')
