import numpy as np
import random
#numero de simulaciones para true y false en change
N = 100
#valores que va a tomar change, TRUE o FALSE
TRUE =1
FALSE = 0
#funcion que crea y cambia de forma aleatoria el orden de la lista
def sort_doors():
	#creacion de la lista
	a = ['goat', 'goat', 'car' ]
	#cambio en el orden
	random.shuffle(a)
	#retorna la nuev lista con orden aleatorio
	return (a)
#funcion que escoge un valor aleatorio de 0 a 2
def choose_door():	
	#creacion de la lista con los valores 0, 1, 2
	a = [0, 1, 2]
	#seleccionar una posicion aleatoria de la lista 
	sel = [random.choice(a)]
	#retornar el valor entero de la lista en esa posicion aleatoria
	return sel[0]
#mostrar una posicion de la lista con valor goat que el jugador no haya escogido
def reveal_door (lista, choice):
	#contador para parar las iteraciones y solamente se cambie el valor de una puerta
	contador = 0;
	#iteraciones a realizar para abrir la puerta
	for i in range(len(lista)):
		#condicion para que se corten las iteraciones si ya se abrio una puerta
		if(contador < 1):
			#condicion para que no se abra la que escogio el jugador
			if (choice!=i):
				#condicion para escoger una puerta en la cual haya una cabra
				if (lista[i] == 'goat'):
					lista[i] = 'GOAT_MONTY'
					contador += 1
	return lista
#funcion en donde el jugador escoge o no cambiar su seleccion y muestra si gano o no
def finish_game(lista, choice, change):
	#el jugador no desea cambiar y se muestra que hay en la puerta
	if (bool(change)==False):
		return lista[choice]
	#el jugador desea cambiar de seleccion
	else:
		#se toma la posicion distinta a la que escogio inicialmente y la que ya se le mostro
		for i in range(len(lista)):
			if (i != choice and lista[i] != 'GOAT_MONTY'):
				#retorna el valor de lo que hay detrás de la puerta nueva escogida
				return lista[i]
#funcion que realiza las N simulaciones si la desicion es (valor) cambiar o no la puerta
def simulaciones(valor, N):
	#lista que va a guardar los distintos resultados detrás de las puertas
	a = []
	for i in range(N):
		#creacion del juego
		lista = sort_doors()
		#numero inicialmente escogido
		choice = choose_door()
		#juego con la revelacion de una puerta
		lista_nueva = reveal_door(lista, choice)
		#resultado del juego
		a.append(finish_game(lista_nueva, choice, valor))
	return a
#realizacion de simulaciones si el jugador quiere cambiar la puerta
atrue = simulaciones(TRUE, N)
#realizacion de simulaciones si el jugador no quiere cambiar la puerta
afalse = simulaciones(FALSE, N)
#variable que guardara la cantidad de veces que el jugador gano o no el carro si decidio cambiar su seleccion
contadortrue = 0
#variable que guardara la cantidad de veces que el jugador gano o no el carro si decidio no cambiar su seleccion
contadorfalse = 0
#iteraciones para contar la cantidad de veces que gano de 100 jugadas
for i in range(N):
	#cantidad de veces que gano si cambio su seleccion
	if (atrue[i]=='car'):
		contadortrue += 1
	#cantidad de veces que gano si no cambio su seleccion 
	if (afalse[i]=='car'):
		contadorfalse +=1
#probabilidad de ganar si cambio su seleccion
probtrue = contadortrue/N
#probabilidad de ganar si no cambio su seleccion
probfalse = contadorfalse/N
print ('la probabilidad de ganar el juego cambiando la puerta es de ', probtrue ,' y la probabilidad de ganar el juego sin cambiar de puerta es de ', probfalse)


