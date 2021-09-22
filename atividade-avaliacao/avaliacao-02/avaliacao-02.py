size = list()
wordlist = list()
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
    print(phrase + " | " + b.join(size))
    size.clear()
    user = str(input("\nPara parar digite 0, para continuar, dê um enter."))
    if user == '0':
        break
biggestword = max(wordlist, key=len)
print("\nThe biggest word is: " + biggestword)
