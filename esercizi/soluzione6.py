'''
***********************PROGRAM_6***********************
CONSEGNA:
data una lista di parole restituisci una nuova lista
contentente solo le parole più lunghe di 5 lettere

***********************INPUT EX (./input6.txt):
mele
pere
banane
salvadanaio
uva
mandarino

***********************OUTPUT EX (./output6.txt):
banane
salvadanaio
mandarino

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

lista = readFile('./input6.txt')
out = []
for prodotto in lista:
  if len(prodotto) > 5:
    out.append(prodotto)

print(out)
saveFile('./output6.txt', out)