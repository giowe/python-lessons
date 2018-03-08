'''
***********************PROGRAM_4***********************
CONSEGNA:
data una lista di numeri moltiplicali per il numero
che li precede e salva la lista aggioranta.
Il primo numero della lista deve essere moltiplicato
per 1.

***********************INPUT EX (./input4.txt):
2
3
5

***********************OUTPUT EX (./output4.txt):
2
6
15

'''

def readFile(fileName): 
  out = []
  file = open(fileName)
  r = file.readlines()
  file.close()

  for e in r:
    out.append(int(e.replace("\n", "")))

  return out

def saveFile(fileName, list):
  file = open(fileName, "w")
  for r in list:
    file.write(str(r) + "\n")
  file.close()

numeri = readFile("./input4.txt")
out = [ numeri[0] ]
for i in range(1, len(numeri)):
  out.append(numeri[i] * numeri[i-1])

saveFile('./output4.txt', out)