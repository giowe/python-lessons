from random import randint

insulti = ['sei una capra', 'sei un semo', 'ignorante!', 'tonto!']
complimenti = ['bravo', 'ottimo', 'sei un pro', 'fuck yea!']

def getRndFromList(lista):
  r = randint(0, len(lista)-1)
  return lista[r]

def insulta():
  print(getRndFromList(insulti))

def complimenta():
  print(getRndFromList(complimenti))

print('Benvenuto nel programma TABELLINE')
t = int(input('Su quale tabellina ti vuoi esercitare?'))

for i in range(11):
	print('Quanto fa', t, 'X', i, '? ')
	risultato = int(input())