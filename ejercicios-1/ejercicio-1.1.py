#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#promedio de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferecia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferecia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferecia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

print("----------------")
print(f'el cursito de daltogod dura un {diferecia_con_min}% menos que el mas rapido')
print(f'el curso de dalto dura un {diferecia_con_max}% menos que el mas lento')
print(f'el curso de dalto dura un {diferecia_con_promedio}% menos que el mas rapido')
print("----------------")

#mosrtrando la cantidad de espacios vacios que se remueven (ejercicio b)
print(f'este curso elimino el {tiempo_vacio_promedio}% de tiempo vacio')
print(f'un curso promedio elimina un   {tiempo_vacio_dalto}% de tiempo vacio')
print("----------------")

#mostrando diferencias si los cursos duraran 10 hs
print (f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 1000 // dalto_curso / 100} horas de otros cursos')
print("----------------")