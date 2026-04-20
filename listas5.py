#lista = [ 2*x for x in [1,2,3,4,5,6,7,8,9,10]]
lista = [ 2*x for x in range(1,10+1)]
print(lista)

#cree una lista de los multiplos de 3 a partir de los valores del 1 al 100
lista = [x for x in range(1, 101) if x % 3 == 0] 
print(lista)

#otra mejorar
lista=[3*x for x in range(1,33+1)] 
print(lista)