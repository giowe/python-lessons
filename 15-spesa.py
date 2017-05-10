carrello = []
negozio = [
  'pane',
  'burro',
  'salame',
  'prodotto costosisssssimo',
  'lattuga',
  'pomodoro'
]

def acquista(indiceProdotto):
  nomeProdotto = negozio[indiceProdotto]
  carrello.append(nomeProdotto)
  return nomeProdotto

def prezzo(nomeProdotto):
  return round(len(nomeProdotto) * 0.1, 2)

def checkout():
  prezzoTotale = 0
  for prodotto in carrello:
    prezzoTotale += prezzo(prodotto)
  return round(prezzoTotale, 2)

print('Benvenuto nel mio modesto negozietto, quele vorresti comperare tra i prodotti che ho da offrire?') 
print('Per concludere l\'acquisto scrivere 666')

for i in range(len(negozio)):
  print(i+1, ')', negozio[i])

while True:
  indiceProdotto = int(input('che prodotto vuoi comperare? '))
  
  if indiceProdotto == 666:
    break
  else:
    prodottoAcquistato = acquista(indiceProdotto-1)    
    print('hai comperato', prodottoAcquistato, 'al modico prezzo di', prezzo(prodottoAcquistato), 'euro')
    print('al momento hai speso', checkout(), 'euro')
    print()

print('grazie per aver fatto la spesa da noi! <3')    
print('puoi pagare in cassa', checkout(), 'euro')
print('hai acquistato:')

for prodotto in carrello: 
  print(prodotto)

