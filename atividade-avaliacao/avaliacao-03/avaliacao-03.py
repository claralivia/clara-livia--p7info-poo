# -*- coding: utf-8 -*-
def primo(p):
 contador = 0
 for i in range(1, p+1):
    if p%i == 0:
        contador = contador + 1
 if contador == 2:
     return True
 else:
     return False
    
def somando(z):
 listt = list()
 x = 0
 while len(listt) < z:
    if primo(x):
        listt.append(x)
    x = x + 1
 soma = sum(listt)
 return soma
    
n = int(input("Digite um número não negativo: "))
print(f"A soma dos primeiros {n} números primos é: {somando(n)}")
