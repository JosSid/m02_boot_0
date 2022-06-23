from functools import reduce

lista = [1, 3, -1, 15, 9]

#map-> Recorre la lista
def f(x):
    return x * 2
    

listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(f, lista)

#filter-> Filtra los elementos de la lista que cumplen la condicion
def esPar(x):
    return x % 2 == 0

listaPares = filter(lambda x: x%2 == 0, lista)
listaPares1 = filter(esPar, lista)

#reduce-> Reduce la lista a un solo elemento
sumatorio = reduce(lambda x,y: x+y,lista)

suma100 = reduce(lambda x,y: x+y, range(101))

sumatorioDobles = reduce(lambda x,y: (x + y*2) , lista)

print(list(listaDobles))
print(list(listaDobles1))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(suma100)
print(sumatorioDobles)