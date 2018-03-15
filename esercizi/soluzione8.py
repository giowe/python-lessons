'''
***********************PROGRAM_8***********************
CONSEGNA:
data una lista di prodotti che contiene dei doppioni
restituisci una lisa di prodotti unici ordinati 
alfabeticamente

***********************INPUT EX (./input8.txt):
mele
pere
mele
mele
cocomeri
pere
cocomeri

***********************OUTPUT EX (./output8.txt):
cocomeri
mele
pere

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

lista = readFile('./input8.txt')
out = []
for prodotto in lista:
  if prodotto not in out:
    out.append(prodotto)

out.sort()

print(out)
saveFile('./output8.txt', out)