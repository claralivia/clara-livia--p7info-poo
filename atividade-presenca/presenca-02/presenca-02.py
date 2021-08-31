import random

def random_numero():
    lista = []
    for i in range(0, 6):
        x = random.randint(1,61)
        lista.append(x)

    return lista

print(*random_numero())