#!/usr/bin/env python
#coding=utf-8


# Exercise 1
#
# Tu tarea consiste en leer y modificar este código
# de manera que se ejecute correctamente, lo único
# que debes cuidar, son las variables y sus declaraciones.

def main():
	var foo;
	print "Hola soy 'foo' y mi valor es 42"
	print "te lo demuestro en esta impresion: %d" % foo

	string duck = raw_input("say cuak cuak: ");

	for i in xrange(5):
		print '\t' * i,
		print "Identar el código es importante"

	String disclaimer = new String("""\n\
En python, la identación de código es más que opcional,
es obligatorio, si tu código no hace lo que quieres,
deberás revisar siempre hacer la identación correcta.

Esto quiere decir, utilizar espacios o tabuladores
(y de preferencia no mezclarlos) cuando quieras hacer
una o más instrucciones dentro de un bloque de código""");
	
	print disclaimer

	$hasta_la_vista_baby = "Fue un gusto haber sido interpretado para ti :')"
	print $hasta_la_vista_baby

if __name__ == '__main__':
	main()