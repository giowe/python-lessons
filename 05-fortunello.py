print('programma protetto da password')
username = input('username: ')
password = input('password: ')
  
if username == 'tizio' and password == 'caio':
  print('accesso effettuato')
  anni = input('quanti anni hai?')

  if anni < 18 or anni > 80:
    print('sei o troppo giovane o troppo anziano')  
  else:
    print('i tuoi anni sono compresi tra 18 e 80')
	
else:  
  print('accesso negato!')

  
print('ciao ciao');