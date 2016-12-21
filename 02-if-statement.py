print('Programma riservato ad utenti maggiorenni')

anni = int ( input('Quanti anni hai? ') )

if anni >= 18:
	delta = anni - 18
	print('sei maggiorenne da', delta, 'anni')
	print('PUOI ENTRARE')
else:
	delta = 18 - anni
	print('sei minorenne ancora per', delta, 'anni')
	print('NON PUOI ENTRARE')