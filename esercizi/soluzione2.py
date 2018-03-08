'''
***********************PROGRAM_2***********************
CONSEGNA:
data una lista di prodotti elimina la cioccolata
e salva la lista aggiornata

***********************INPUT EX (./input2.txt):
mele
cioccolata
banane

***********************OUTPUT EX (./output2.txt):
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

carrello = readFile("./input2.txt")
while "cioccolata" in carrello:
  carrello.remove("cioccolata")

saveFile("./output2.txt", carrello)
