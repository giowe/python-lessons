materia = input('Dimmi di che materia stiamo parlando? ')

listaVoti = []
while True:
	votoCorrente = float(input('inserisci un voto: '))
	if votoCorrente > 10 or votoCorrente < 0:
		print('hai inserito', votoCorrente,', non è un valore accettabile.')
	elif votoCorrente == 0:
		break
	else:
		listaVoti.append(votoCorrente)

nVoti = len(listaVoti)
sommatoria = sum(listaVoti)
media = sommatoria / nVoti
print('Fino ad ora in', materia, 'hai preso', nVoti, 'voti la cui media è', media)			

print('Tutti i voti che hai preso in', materia, 'sono:')
for voto in listaVoti:
	print(voto)
