#!/usr/bin/env python
#coding=utf-8
from random import shuffle as mix
import random

meximons = {
	"Nopalsaur": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Charmando": {'ubicacion': "Las montañas armadas", 'peso': "4 costales de frijoles", 'descripcion': "Un dragón (que si puede volar), tiene una pequeña flama en su cola, si esta se apaga, Charmando perderá la memoria y con ella su experiencia en batallas."},
	"Chinrizard": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Skirtlu": {'ubicacion': "Mar 'donde la vida es más sabrosa'", 'peso': "40 papas", 'descripcion': "Una tortuga (que parece asfixiada), esencial para la escases de agua en África, por lo que no la encontrarás allá."},
	"Wartorta": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Caterpio": {'ubicacion': "Fábricas de nor suiza", 'peso': "2 caterpios", 'descripcion': "Un pollo que frecuentemenete confunden con una oruga (aún no sabemos por qué), tiene habilidades culinarias."},
	"MetaiPod": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Buttercaught": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Ratota": {'ubicacion': "Cocinas de las Marias", 'peso': "1 caja de zapatos", 'descripcion': "Misterioso ratón, jamás ha sido visto por el Dr. Koopa, pero se cree que éste capturaría a María en su castillo en caso de verlas."},
	"Espirrow": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"FeatRow": {'ubicacion': "Montañas 'Ya tu sabe'", 'peso': "1 gas tank", 'descripcion': "Ave con extraorinarias cuerdas vocales. Se presume que ha colaborado con Ranstein y Tocálica en 'El sonidito+'"},
	"Snake": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Arbobra": {'ubicacion': "India", 'peso': "Lo mismo que una kobra real", 'descripcion': "Serpiente tipo venenoso, se le nombró así porque es lo último que decían las personas al ser mordidas por ésta."},
	"PicaAchu": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Ranchu": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Sandalew": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Nidoreina": {'ubicacion': "Pais de las maravillas", 'peso': "1 corona + 50Kg", 'descripcion': "Una completa diva, se negó a describirse a sí misma"},
	"Nacoqueen": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"NueveColas": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Jajapuff": {'ubicacion': "Noches de Humor con Ramón", 'peso': "0.5 Kg", 'descripcion': "Meximón del tipo comediante, si escuchas sus chistes, te hará llorar sangre, por lo que se recomienda mantener distancia."},
	"Zuba": {'ubicacion': "Cuevas esqüirt", 'peso': "Un caballero del a noche", 'descripcion': "Murcielago diabético, generalmente lo encuentras en los manantiales de uva dentro de la cueva."},	
	"Miglett": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Dugpack": {'ubicacion': "No disponible", 'peso': "4 veces un Miglett", 'descripcion': "Miglett versión tetrapack."},
	"Miau": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Persión": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Arcadiez": {'ubicacion': "Volcan hulawula - Hawai", 'peso': "2 costales de lava", 'descripcion': "Evolución de Grewlithe, aunque Grewlithe no ha sido descubierto, ya encontramos a Arcadiez, tipo fuego-mordelón."},
	"Acadabra": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"HocusPocus": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Maricarp": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Machete": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Machetote": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Tentaculei": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Gravael": {'ubicacion': "Montañas rocosas", 'peso': "1000 Kg", 'descripcion': "Como una piedrita en el zapato, pero más pesada."},
	"Ponytaba": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Rapidaaash": {'ubicacion': "Velódromos Vazquez", 'peso': "Desconocido", 'descripcion': "Una llegua muy muy fresa, corre por presumir sus tersas patas, si le das un chile, su crin se torna color morado."},
	"Estaryu" : {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Synx": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Riito": {'ubicacion': "Papelerias 'el cometa'", 'peso': "50 gr.", 'descripcion': "Meximón asexual, aún así, puedes usarlo para obtener huevos meximón y convertirte en granjero."},
	"Sdorlax": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Dragoday": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Mewthree": {'ubicacion': None, 'peso': None, 'descripcion': None},
	"Abogado": {'ubicacion': "Camara de senadores, juzgados y cualquier lugar donde se pueda transear gente", 'peso': "La ley", 'descripcion': "Tipo tranza, aléjate de él a toda costa. Se dice que le costó a Merceus (PokeDios) deshacerce de ellos enviandolos a la Tierra."}
}
copy = meximons.copy()
meximon_sin_datos = True


def dame_meximon():
	for key in copy:
		return (key, copy.pop(key))


def set_meximon(llave,datos):
	meximons[llave] = datos


def actualiza_dicciodex():
	meximon_sin_datos = False
	for key in meximons:
		if meximons[key]['ubicacion'] == None:
			meximon_sin_datos = True
			break


def main():
	"""not made for direct call"""
	print("Error: código no apto para llamada directa")
	exit(1)


if __name__ == '__main__':
	main()
