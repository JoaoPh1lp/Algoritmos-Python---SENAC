## Crie uma função que calcule o fatorial de um número (sem usar recursão).

import math

def num_fatorado():
    num = int(input("Digite um número para vê-lo fatorado: "))
    print(f"O fatorial de {num} é {math.factorial(num)}")
num_fatorado()