import numpy as np
import random
N = 100
TRUE =1
FALSE = 0
def sort_doors():
	a = ['goat', 'goat', 'car' ]
	random.shuffle(a)
	return (a)
def choose_door():	
	a = [0, 1, 2]
	sel = [random.choice(a)]
	return sel[0]
def reveal_door (lista, choice):
	contador = 0;
	for i in range(len(lista)):
		if(contador < 1):
			if (choice!=i):
				if (lista[i] == 'goat'):
					lista[i] = 'GOAT_MONTY'
					contador += 1
	return lista
def finish_game(lista, choice, change):
	if (bool(change)==False):
		return lista[choice]
	else:
		for i in range(len(lista)):
			if (i != choice and lista[i] != 'GOAT_MONTY'):
				return lista[i]
def simulaciones(valor, N):
	a = []
	for i in range(N):
		lista = sort_doors()
		choice = choose_door()
		lista_nueva = reveal_door(lista, choice)
		a.append(finish_game(lista_nueva, choice, valor))
	return a
atrue = simulaciones(TRUE, N)
afalse = simulaciones(FALSE, N)
contadortrue = 0
contadorfalse = 0
for i in range(N):
	if (atrue[i]=='car'):
		contadortrue += 1
	if (afalse[i]=='car'):
		contadorfalse +=1
probtrue = contadortrue/N
probfalse = contadorfalse/N
print ('la probabilidad de ganar el juego cambiando la puerta es de ', probtrue ,' y la probabilidad de ganar el juego sin cambiar de puerta es de ', probfalse)


