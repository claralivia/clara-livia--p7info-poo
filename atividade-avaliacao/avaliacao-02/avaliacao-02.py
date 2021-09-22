size = list()# lista para receber o tamanho de cada palavra
wordlist = list()
i = a = 0
biggestword = 0
b = "-"
while True:
    phrase = str(input("\nDigite uma frase? "))  # recebendo a frase
    words = phrase.split()  # dividindo as palavras
    for i in words:
        size.append(str(len(i))) # adicionando o tamanho de cada palavra
        wordlist.append(i) # adicionando cada palavra em uma lista
        if len(i) >= a:
            a = len(i)
            biggestword = i
    print(phrase + " | " + b.join(size))
    size.clear()
    user = str(input("\nPara parar digite 0, para continuar, dê um enter."))
    if user == '0':
        break
biggestword = max(wordlist, key=len) #pegando a palavra de maior tamanho
print("\nThe biggest word is: " + biggestword)
