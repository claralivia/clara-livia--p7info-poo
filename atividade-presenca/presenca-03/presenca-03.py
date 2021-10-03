pilha = ['apple', 'cherry', 'grape', 'lemon', 'melon']
print("Pilha: ", pilha)

def inserir(nome):
    pilha.append('orange')
    print('\nInserindo um elemento: ', pilha)

def remover():
    pilha.pop()
    print('\nRemovendo um elemento:', pilha)

inserir('orange')
remover()

print("\nPilha: ", pilha)
