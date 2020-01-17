#es.1 scrivi l'output del seguente programma:
lista = ['a', 'b', 'c']
for lettera in lista:
    for i in range(3):
        print(i, lista[i])

#es.2 quale valore deve avere x perchè l'output sia 4
a = 3
b = 5
if a > 3:
    print(x - a + b)
else:
    print(a - x + b)        

#es.3 scrivi l'output del seguente programma:
for i in range(3):
    for l in range(2):
        print(i*l)

#es.4 quale valore devono avere S ed E perchè l'output del programma sia 2 3 4 5
for i in range(S, E):
    print(i+2)

#es.5 quale output ottengo dal seguente programma:
lista = ['a', 'b', 'c']
print(lista[len(lista)-1])
for i in range(3):
    print(lista[i])
    for l in range(3):
        print(i, l, lista[i], lista[l])
    print('---')
print('end.')

#es 6 quale output ottengo dal seguente programma:
lista = ["a", "b", "c"]

for i in range(len(lista)):
    print(i, lista[i])
 
#es 7 quale output ottengo dal seguente programma:
for i in range(5, 7):
    print(i - 1)

#es 8 quale output ottengo dal seguente programma:
i = 0
while i < 10:
    print(i)

#es 9 quale output ottengo dal seguente programma:
for i in range(1, 4):
    if i > 2:
        print("ciao")
    else:
        print(i + i - 1)

#es 10 quale output ottengo dal seguente programma:
for x in range(3):
    for y in range(3):
        for z in range(2):
            print(x + y + z)

#es 11 quale output ottengo dal seguente programma:
lista = ["a", "b", "c"]
while len(lista) > 0:
    print(lista.pop())
  
#es 12 quale output ottengo dal seguente programma:            
lista = [1]
while len(lista) > 0:
    n = lista.pop()
    print(n)
    lista.append(n+1)

#es 13 quale output ottengo dal seguente programma:    
for x in range(2):
    print("---")
    for y in range(25, 27):
        if y % 2 == 0:
            print(y + x)
        else:
            print(y - x) 
    print("---")
    
#es 14 quale output ottengo dal seguente programma:    
lista = []

while True:
    lista.append(len(lista))
    if len(lista) > 3 and lista[-1] % 2 == 0:
        break
    
for e in lista:
    print(e)
   
#es 15 quale output ottengo dal seguente programma:    
lista = ["ciao", "mare"]
lista2 = []

for p in lista:
    p2 = ""
    for l in p:
        p2 = l + p2
    
    lista2.append(p2)
    
for p in lista2:
    print(p)

