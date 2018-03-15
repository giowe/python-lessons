'''
***********************PROGRAM_5***********************
CONSEGNA:
data una lista di numeri seleziona solo quelli maggiori
di 5 e minori di 10

***********************INPUT EX (./input5.txt):
1
6
5
34
10
8

***********************OUTPUT EX (./output5.txt):
6
8

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

'''
lista = [
  1,
  6,
  5,
  34,
  10,
  8
]
'''
lista = readFile('./input5.txt')
out = []
for numero in lista:
  if numero > 5 and numero < 10:
    out.append(numero)

print(out)
saveFile('./output5.txt', out)