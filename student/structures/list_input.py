#!/usr/bin/env python
#coding=utf-8
from random import shuffle as mix
from string import ascii_letters as letters
from random import choice as c

#lista = [i for i in range(100)]
lista = [i for i in [c(range(100)) for i in range(100)]]
mix(lista)
lista2 = [i for i in [c(letters) for i in range(len(letters))]]

def main():
	"""not made for direct call"""
	print("Error: código no apto para llamada directa")
	exit(1)

if __name__ == '__main__':
	main()