from random import randint
t = int(input('su quale tabellina vuoi esercitarti? '))

while True:
  giuste = 0
  tentativi = 0
  while giuste < 3:
    tentativi +=1
    r = randint(0, 10)
    risp = int(input('quanto fa ' + str(t) + ' x ' + str(r) + '? '))
    if risp == t*r:
      giuste += 1
      print('bene!')
    else:
      print('ma no! Il risultato è', t*r)

  if tentativi == 3:
    print('perfetto')
    break
  elif tentativi > 3 and tentativi <= 5:
    print('mmm facciamo che vai a ripassare')
    break
  else:
    print('riparti!')
