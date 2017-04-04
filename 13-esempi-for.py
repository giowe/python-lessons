nomi = ['tizio', 'caio', 'sempronio']

for nome in nomi:
	print ('il nome selezionato è', nome)

frutta = ['pera', 'mela', 'banana']	

print('La mela si trova all\' indice', frutta.index('mela'))

for frutto in frutta:
	print('nel carrello metto una', frutto)

print('lista della spesa:')
for i in range(len(frutta)):
	print(i+1, ')', frutta[i])

for lettera in 'CIAONE':
	print('DATEMI UNA ', lettera, '!!!')
print('CIAONE!!!')



errori = 0
for i in range(0, 11):
	print('quanto fa 3 X', i, '?')
	r = int(input())
	if r == 3*i:
		print('BRAVO!')
	else:
		print('CAPRA!')	
		errori += 1

	if errori == 3:
	  print('BASTA! Sei troppo scarso, torna quando hai studiato!')	
	  break