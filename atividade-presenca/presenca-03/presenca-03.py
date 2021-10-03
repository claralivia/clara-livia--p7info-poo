pilha = list()
print("Pilha: ", pilha)

def inserir(nome):
    pilha.append(nome)
    print(f'\nInserindo o elemento {nome}: ' + ' '.join(pilha))

def remover():
    pilha.pop()
    print('\nRemovendo um elemento: ' + ' '.join(pilha))

inserir('orange')
remover()

print('\nPilha: ' + ' '.join(pilha))
