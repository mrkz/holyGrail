#!/usr/bin/env python
# coding=utf-8

# TL;DR: Para más información teclea help('list') en el interprete python

# Listas
# Contienen un conjunto de elementos no necesariamente del mismo tipo.
# Las pilas y colas son implementaciones de listas, por lo que
# una estructura pila o cola en Python se hace presente con una lista
# implementando los método pop, append e insert.
# Son objetos iterables al igual que las tuplas y los diccionarios.
# Pueden contener objetos dentro de de ellas tales como
# Listas, Tuplas, Diccionarios, Objetos definidos por el programador, etc.

lista_valida = ["Cafe", 42, "Tacvba", 100, "años de soledad", [3, 1, 4], (3.14159,)]


# Pueden ser iteradas con un for, en cada iteración se toma el valor
# del siguiente elemento en la lista, hasta que esta quede vacía
def itera_lista(lista):
	print("\nIterando lista:")
	for elemento in lista:
		print(elemento)


# Si deseas invertir una lista, utiliza el método reverse()
def invierte_lista(lista):
	print("\nInvirtiendo lista:")
	lista.reverse()
	print(lista)


# Para ordenar una lista, utiliza el método sort()
def ordena_lista(lista):
	lista.sort()
	print(lista)


# Para insertar elemento en una lista en indice N, utiliza método insert()
def inserta_en_lista(lista, elemento = None, indice = 0):
	lista.insert(indice, elemento)

# bla bla bla
# and so on con los métodos de la clase lista.
# Para más información, leer el TL;DR de la línea 4


def main():
	"""Soy main, y esta es mi documentación"""
	print('# Listas'
		  '# Contienen un conjunto de elementos no necesariamente del mismo tipo.\n'
		  '# Las pilas y colas son implementaciones de listas, por lo que\n'
		  '# una estructura pila o cola en Python se hace presente con una lista\n'
		  '# implementando los método pop, append e insert.\n'
		  '# Son objetos iterables al igual que las tuplas y los diccionarios.\n'
		  '# Pueden contener objetos dentro de de ellas tales como\n'
		  '# Listas, Tuplas, Diccionarios, Objetos definidos por el programador, etc.')
	print("lista_valida =", lista_valida)
	itera_lista(lista_valida)
	invierte_lista(lista_valida)


if __name__ == '__main__':
	main()
