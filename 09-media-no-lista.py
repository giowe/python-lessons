materia = input('Dimmi di che materia stiamo parlando? ')

sommatoria = 0
nVoti = 0

while True:
	votoCorrente = float(input('inserisci un voto: '))
	if votoCorrente > 10 or votoCorrente < 0:
		print('hai inserito', votoCorrente,', non è un valore accettabile.')
	elif votoCorrente == 0:
		break
	else:
		nVoti += 1
		sommatoria += votoCorrente

media = sommatoria / nVoti
print('Fino ad ora in', materia, 'hai preso', nVoti, 'voti la cui media è', media)			