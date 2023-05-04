#!/usr/bin/env python
#coding=utf-8

# VARIABLES
#
# Las variables en python siguen la sintaxis C 
# al momento de ser utilizadas; es decir:
# Inician con caracter: {_,lowercase, uppercase}
#
# DECLARACION DE VARIABLES
#
# Estas no necesitan ser declaradas, esto significa
# que pueden ser instanciadas al momento de usarlas,
# si no existe, se crea; si existe, se sobre-escribe.


def main():
	foo = "Hola!, soy la variable 'foo' y soy una cadena"
	print(foo)
	foo = "ahora 'foo' es otra cadena"
	print(foo)
	var = """\
Soy una cadena de tipo parrafo,
tal como me escriben, es como aparezco



¿lo ves?"""
	print(var)
	# cambiando el tipo de 'var'
	var = 42

	# También podemos utilizar el pre-formateo tipo C
	print("The answer to the life, the universe and everything is %d" % var)


if __name__ == '__main__':
	main()
