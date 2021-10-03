pilha = ['apple', 'cherry', 'grape', 'lemon', 'melon']
print("Pilha: ", pilha)

def inserir(nome):
    pilha.append(nome)
<<<<<<< HEAD
    print(f'\nInserindo o elemento {nome}: ' + ' '.join(pilha))
=======
    print('\nInserindo um elemento: ', pilha)
>>>>>>> a2a2f78b75c9464e91f2eaa9fdf32985b17fe84e

def remover():
    pilha.pop()
    print('\nRemovendo um elemento: ' + ' '.join(pilha))

inserir('orange')
remover()

print('\nPilha: ' + ' '.join(pilha))
