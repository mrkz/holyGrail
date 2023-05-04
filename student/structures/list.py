#!/usr/bin/env python
# coding=utf-8

# Exercise 3
# El trabajo en este ejercicio consiste en unir las listas 
# presentadas en las variables 'lista' y 'lista2', omitiendo
# aquellos elementos que se repitan dentro de la mismas, generando
# así una sola lista sin elementos repetidos.

# por ejemplo:
# sea 'lista' = [1, 2, 3, 4, 8, 9, 42, 100]
# y 'lista2' = ["Pedro", "Juan", 100, 1, 42]
# la lista resultante sea = [1, 2, 3, 4, 8, 9, 42, 100, "Pedro", "Juan"]
# (no necesariamente en el mismo orden)
from list_input import lista, lista2


# Hint: para saber si tu lista generada repite elementos
# utiliza la siguiente función, te dirá qué elementos se repiten
# (y cuántas veces), envia tu lista como parámetro.
def revisa_repeticiones(wish_list):
	flag = False
	wish_list.sort()
	last_element = None
	for element in wish_list:
		k_veces = wish_list.count(element)
		if (last_element != element) and k_veces > 1:
			print("'%s' se repite %d vece(s)" % (element, k_veces))
			flag = True
		last_element = element
	if not flag:
		print("Felicidades, tu lista no repite ningún elemento \o/")

# escribe tu código a partir de aquí


def main():
	# llama a tus funciones y haz tu mágia.
	revisa_repeticiones(lista2)


if __name__ == '__main__':
	main()
