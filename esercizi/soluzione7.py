'''
***********************PROGRAM_7***********************
CONSEGNA:
data una lista composta da due numeri seguiti dal
nome di vari prodotti, ricava un sottoinsieme della
stessa usando come estremi della nuova lista i due 
numeri sopracitati.
Dalla lista così ottenuta rimuovi tutti i prodotti
che iniziano con la lettera "p" (ricordo che le 
stringhe hanno moltissimi aspetti in comune con
le liste)

***********************INPUT EX (./input7.txt):
2
5
mele
pere
banane
cocomeri
mele
pere
pere

***********************OUTPUT EX (./output7.txt):
mele
banane

'''

def readFile(fileName): 
  out = []
  file = open(fileName)
  r = file.readlines()
  file.close()

  for e in r:
    out.append(e.replace("\n", ""))

  return out

def saveFile(fileName, list):
  file = open(fileName, "w")
  for r in list:
    file.write(str(r) + "\n")
  file.close()

'''
lista = [
  '2',
  '5',
  'mele',
  'pere',
  'banane',
  'cocomeri',
  'mele',
  'pere',
  'pere'
]
'''
lista = readFile('./input7.txt')

primoNumero = int(lista[0])
secondoNumero = int(lista[1])
sottoLista = lista[primoNumero : secondoNumero]
listaFinale =  []
for prodotto in sottoLista:
  if prodotto[0] != 'p':
    listaFinale.append(prodotto)

saveFile('./output7.txt', listaFinale)
print(listaFinale)