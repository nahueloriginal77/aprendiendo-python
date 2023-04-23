diccionario = {
    "nombre" : 'lucas',
    "apellido" : 'dalto',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get () (si no se encuentra nada el prigrama continua)
valor_de_kasadks = diccionario.get("kasadks")

#eliminando todo del dicccionario
#diccionario.clear()

#eliminando un elemento del dicc
diccionario.pop("apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)






