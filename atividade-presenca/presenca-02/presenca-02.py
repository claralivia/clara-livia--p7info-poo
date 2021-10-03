# -*- coding: utf-8 -*-
def printDecimal(dec):
    return dec

def printOctal(o):
    oct = format(o, "o")
    return oct

def printHexadecimal(h):
    hex = format(h, "x")
    return hex

def printBinario(b):
    bin = format(b, "b")
    return bin

def imprimirTabela(d, o, h, b):
    return("{:<9d} {:>9s} {:>15s} {:>26s}".format(d, o, h, b))


print("{:<9s} {:>9s} {:>15s} {:>26s}".format('Decimal', 'Octal', 'Hexadecimal', 'Binário'))
for i in range(0, 70):
      print("-", end="")
print("\n", end="")
for x in range(0, 256):
    print(imprimirTabela(printDecimal(x), printOctal(x), printHexadecimal(x), printBinario(x)))
