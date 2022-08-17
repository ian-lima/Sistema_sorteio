# Crie um programa que gera um número de 1 a 10;
# Peça para o usuário adivinhar o número;
# E identifique se ele acertou ou não;

import random

adivinhe = random.randint(1,10)

escolhanum = int(input("Escolha seu número de 1 a 10: "))

if escolhanum == adivinhe:
    print("Você acertou! O número é: %d" % adivinhe)
else:
    print("Você errou! O número era: %d" % adivinhe)