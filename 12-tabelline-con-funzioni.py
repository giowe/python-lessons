from random import randint, shuffle

print('Programma tabelline')

insulti = ['semo', 'piva', 'pirla', 'esen']
complimenti = ['bravo', 'wow', 'ottimo!', 'WTF!!!!', '<3 <3 <3']

def get_rnd_from_list(lista):
	r = randint(0, len(lista)-1)
	return lista[r]	

def insulta():
	insulto = get_rnd_from_list(insulti)
	return insulto

def complimenta():
	complimento = get_rnd_from_list(complimenti)
	return complimento

t = int(input('su quale tabellina ti vuoi esercitare?'))

numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(numeri)

while True:
	voto = 0
	for n in numeri:
		print('quanto fa', t, 'X',n,'?')
		risp = int(input())
		if risp == n * t:
			print(complimenta())
			voto += 1
		else:
			print(insulta())

	if voto >= 6 and voto < 11:
		print(complimenta())
		print('Ok, non male... poteva andare meglio ma di sicuro non sei', insulta())
		break
	elif voto < 6:
		for x in range(3):
			print(insulta())
		print('Oggi mi sa che sara`una lunga giornata... riparti da capo')	
	else:
		for x in range(5):
			print(complimenta())
		print('Sei il mio allievo preferito! sei un mega maestro della tabellina del', t)
		break