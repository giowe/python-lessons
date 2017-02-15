from random import randint
min = 1
max = 100
numeroSegreto = randint(min, max)
tentativi = 0
print("indovina a quale numero sto pensando tra",min,"e",max)

while True:
  tentativi += 1
  numeroUtente = int(input("inserisci un numero: "))
  
  if numeroUtente > numeroSegreto:
    print(numeroUtente, "e' troppo grande")
  elif numeroUtente < numeroSegreto:
    print(numeroUtente, "e' troppo piccolo")
  else:
    break

print("HAI INDOVINATO IN", tentativi, "TENTATIVI")
if tentativi > 10:
  print("non sei particolarmente forte eh...")
else:  
  print("sei stato forte!")
