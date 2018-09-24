#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
import os

def generar_palindromo(numero, palindromo, historial):

	historial.write(palindromo + "\n")
	print(palindromo)


	pal = ""

	if(numero > 1):

		numero = numero - 2

		for i in palindromo:
			if(i!= "s"):
				pal = pal + i

			else:
				opc = random.randint(0,1)
				if(opc):
					pal = pal + "0s0"
				else:
					pal = pal + "1s1"

			palindromo = pal
	
		return generar_palindromo(numero, palindromo, historial)

	else:

		eps = False

		for j in palindromo:

			if( j != "s"):
				pal = pal + j

			else:
				opc = random.randint(1,3)
				if( opc == 1):
					pal = pal + "0"
				elif (opc == 2):
					pal+="1"
				else:
					eps = True
					continue
		if(eps):
			pal+= "    Se agregó la cadena vacía ε"

		palindromo = pal
		return palindromo



def main():

	historial = open("Historial.txt", "w+")
	historial.close()

	while(True):


		os.system('clear')

		print("	    --PROGRAMA DE GENERACIÓN DE PALINDROMOS--\n")
		print("1) Generar una cadena con un número aleatorio")
		print("2) Ingresar el tamaño de la cadena")
		print("3) Salir ")

		opc = raw_input("-->")
		os.system('clear')

		if(opc == "1" or opc == "2"):
			historial = open("Historial.txt", "w+")


		if(opc == "1"):
			historial.write("\t\t\tProceso de derivación  \n\n")
			palindrome = generar_palindromo(random.randint(1,20), "s", historial)
			print("El palindromo generado fue: " + palindrome)
			historial.write("El palindromo generado fue: " + palindrome)
			raw_input()

		elif (opc == "2"):
			try:
				tam = int(raw_input("Ingrese el tamaño: "))
				if(tam < 1):
					raw_input("\nNúmero no valido, inténtalo de nuevo")
					os.system('clear')
					continue

			except:
				raw_input("\nNo valido, inténtalo de nuevo")

				continue

			palindrome = generar_palindromo(tam, "s", historial)
			print("El palindromo generado fue: " + palindrome)
			historial.write("\nEl palindromo generado fue: " + palindrome)
			raw_input()

		elif (opc == "3"):
			break

		else:
			raw_input("\nOpción no valida")

		historial.close()
	
main()