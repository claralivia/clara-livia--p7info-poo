# -*- coding: utf-8 -*-
size = list()
wordlist = list()
table = list()
i = a = 0
biggestword = 0
b = "-"
while True:
    phrase = str(input("\nDigite uma frase: "))
    words = phrase.split()
    for i in words:
        size.append(str(len(i)))
        wordlist.append(i)
        if len(i) >= a:
            a = len(i)
            biggestword = i
    table.append("\n{:<50} | {:>20}".format(phrase, b.join(size)))
    size.clear()
    user = str(input("Para parar digite 0, para continuar, dê um enter. "))
    if user == '0':
        break
    
print("\n{:<50} | {:>20}".format('Frase', 'Letras por palavra'))
for i in range(0, 100):
      print("-", end="")
print(*table)
print("A maior palavra é: " + biggestword)
