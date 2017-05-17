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

#es.5 quele output ottengo dal seguente programma:
lista = ['a', 'b', 'c']
print(lista[len(lista)-1])
for i in range(3):
    print(lista[i])
    for l in range(3):
        print(i, l, lista[i], lista[l])
    print('---')
print('end.')
