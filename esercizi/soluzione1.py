def readFile(fileName): 
  out = []
  file = open(fileName)
  r = file.readlines()
  file.close()

  for e in r:
    out.append(int(e.replace("\n", "")))

  return out

somma = 0
for numero in readFile('./input1.txt'):
  somma += numero

file = open('./output1.txt', 'w')
file.write(str(somma))
file.close()