print('inserisci il nome utente e la password fino a che non sono corretti')

username = ''
password = ''
tentativi = 0
while username != 'tizio' or password != 'caio':
	tentativi += 1

	username = input('USERNAME: ')
	password = input('PASSWORD: ')
	if (username != 'tizio' or password != 'caio'):
		print('USERNAME O PASSWORD NON CORRETTI! RIPROVA')

print('ACCESSO EFFETTUATO IN',tentativi,'TENTATIVI')		