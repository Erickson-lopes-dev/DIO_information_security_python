import itertools

string = input("String a ser permutada: ")

# fara permutação dos caracteres la no worlist
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))
