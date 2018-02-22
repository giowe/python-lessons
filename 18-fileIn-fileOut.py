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

carrello = readFile("./18-input-file.txt")

for e in carrello:
  print(e)

print("aggiungo cioccolata al carrello e salvo il file")
carrello.append("cioccolata")
saveFile("./18-output-file.txt", carrello)