#!/usr/bin/env python
# coding=utf-8

# Variables Globales
# Deben ser especificadas en caso de ser utilizadas
# localmente por alguna función

foo = 14


def deep_tought(foo=999):
	print("el valor de 'foo' es", foo)
	earth()


def earth():
	global foo
	print("el valor de 'foo' es", foo)


def main():
	"""Soy main, y esta es mi documentación"""
	deep_tought()


if __name__ == '__main__':
	main()
