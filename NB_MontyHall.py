import numpy as np
import random
a = [0,1]
change = random.choice(a)
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
