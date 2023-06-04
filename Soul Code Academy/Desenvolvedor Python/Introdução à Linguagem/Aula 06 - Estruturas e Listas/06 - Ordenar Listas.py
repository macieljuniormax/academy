lista = ["a", "x", "s", "w", "d", "a", "n", "b", "p"]

lista2 = lista[:]
lista2.reverse()
print(lista2)

lista3 = lista[:]
lista3.sort()
print(lista3)

for i in range(len(lista)):
    print(lista[i])

for j, k in enumerate(lista):
    print(j, k)

quantidade = lista.count("a")
print(quantidade)

