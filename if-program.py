print('Questo programma è riservato agli utenti maggiorenni')
anni = int( input('Quanti anni hai? ') )

print('hai', anni, 'anni')

if anni >= 18:
	delta = anni - 18
	print('SEI MAGGIORENNE da', delta)
	print('puoi entrare!!!')

else:
	delta = 18 - anni
	print('SEI MINORENNE ancora per', delta)
	print('stai fuori!')
