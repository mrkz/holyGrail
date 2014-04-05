#!/usr/bin/env python
# coding=utf-8
from dict_input import meximons, dame_meximon, meximon_sin_datos, copy, set_meximon
# Exercise 4
#
# El trabajo en este ejercicio consiste en convertirte en un maestro
# Meximón, en el proceso deberás completar la dicciodex, una versión
# alterada del mexidéx, ya que este te brindará el nombre del meximón
# y tu deberás llenar sus datos básicos.
#
# Sin embargo, ser un maestro Meximón no es cosa sencilla, pues hay
# Meximones que ya son conocidos (¿quién no ha encontrado un maricarp?)
# y sus datos no deben ser sobre-escritos, pues estos están sometidos a
# derechos de autor fijados por el maligno Dr.Koopa Traloosa.
# En caso de existir los datos de éste Meximon, deberás mostrarlos (pues el
# dicciodex siempre muestra información del Meximón que aparece).
#
# La meta es completar la dicciodex sin pasar por demandas del Dr. Koopa
# en el proceso

# por ejemplo:
#
# Charmando salvaje ha aparecido!
# Ubicación: Las montañas armadas
# Peso:  4 costales de frijoles
# Descripción: Un dragón (que si puede volar), tiene una pequeña flama
#  en su cola, si esta se apaga, Charmando perderá la memoria y con ella
#  su experiencia en batallas.

# Esta es una descripción del malvado Dr. Koopa, el dicciodex está un poco
# mal programado (Gracias, Dr. Oka), por lo que deberás modificarlo para
# evitar a toda costa contratar un abogado (ya éste tipo de Meximón es del 
# tipo tranza).

# Hint: si al querer acceder a algún dato del meximón, el valor de éste es
# None, ¡Podrémos ganarle al Dr. Koopa Traloosa éste descubrimiento!

# Hint 2: La estructura en el dicciodex es la siguiente:
# { 
#	Meximón: {'ubicación':<valor>, 'peso': <valor>, 'descripcion': <desc>},
#	Meximón: {'ubicación':<valor>, 'peso': <valor>, 'descripcion': <desc>},
# }

# dame_meximon() => regresa una tupla con los valores (llave, {datos})
def wild_meximon():
	meximon = dame_meximon()
	print """\
%s salvaje ha aparecido!
 Ubicación: %s
 Peso: %s
 Descripción: %s
""" % (meximon[0],
	   meximon[1]['ubicacion'],
	   meximon[1]['peso'],
	   meximon[1]['descripcion'])
	raw_input()


def modifica_meximon(llave, datos):
	if llave in meximons and datos.has_key('ubicacion') and\
	   datos.has_key('peso') and datos.has_key('descripcion'):
	   set_meximon(llave,datos)
	else:
		print "Datos para el dicciodex no válidos"

# Escribe tu código a partir de aquí



def main():
	# llama a tus funciones y haz tu mágia.
	while len(copy) > 0 and meximon_sin_datos:
		wild_meximon()
	

if __name__ == '__main__':
	main()