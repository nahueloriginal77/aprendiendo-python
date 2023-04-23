#creando una lista con list()
lista = list(["hola","dalto",34])


#devuelve la cantidad de elementos de la lista
resultado =len(lista)

#agregando un elemento a la lista
lista.append("tuvieja")

#agregando un elemento a la lista con un indice especifico
lista.insert(1,"uh")

#agregando varios elementos
lista.extend([False,2030])

#eliminando  un elemento de la lista
lista.pop(-1) #-1 para eliminar el ultimo

#removiendo un elemento de la lista por su valor
lista.remove("uh")

#eliminando todos los elementos de la lista
#lista.clear()

lista.remove("hola")
lista.remove("dalto")
lista.remove("tuvieja")
lista.remove(False)
lista.extend([1,2,77,11,9])

#ordenando la lista(si usamos el parametro reverse se ordena al reves)
lista.sort(reverse=True)
lista.reverse()

#verificando si un elemento en la lista
elemento_encontrado = lista.index(1)
print()




