'''
***********************PROGRAM_3***********************
CONSEGNA:
data una lista di numeri moltiplicali per due e salva
la lista aggioranta

***********************INPUT EX (./input3.txt):
2
3
5

***********************OUTPUT EX (./output3.txt):
4
6
10

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

numeri = readFile("./input3.txt")

#metodo più facile da capire
numeriX2 = []
for n in numeri:
  numeriX2.append(n*2)

#metodo alternativo (preferibile)
#for i in range(len(numeri)):
#  numeri[i] *= 2

saveFile("./output3.txt", numeriX2)
