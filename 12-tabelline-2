from random import randint, choice

insulti = ["pirla", "ignorante", "capra", "semo"]
complimenti = ["bravo", "ottimo", "sei un genio", "mo che bravo!", "dio te stradora!"]

print("programma tabelline!")
t = int(input("su quale tabellina vuoi esercitarti?"))

while True:
  count_giuste = 0
  count_totali = 0

  while count_giuste < 3:
    r = randint(0, 10)
    risultato = int(input("quanto fa {} x {} = ".format(t, r)))

    count_totali += 1
    if risultato == r * t:
      print("corretto! {}".format(choice(complimenti)))
      count_giuste += 1
    else:
      print("sbagliato! {}".format(choice(insulti)))
      count_giuste = 0

  print("abbiamo finito per oggi!")

  def stampaTabellina(tabellina, fino_a_che_numero = 11):
    for n in range(fino_a_che_numero):
      print("{} x {} = {}".format(n, tabellina, n*tabellina))

  if count_totali == 3:
    print("sei un fenomeno, padroneggi divinamente la tabellina del {}".format(t))
    print("a questo punto, studiati fino al 20!")
    stampaTabellina(t, 21)
    break
  elif count_totali < 5:
    print("diciamo che te la cavi ma meglio se ripassi un attimo, guarda qui:")
    stampaTabellina(t)
    break
  else:
    print("mamma mia... studia!")
    stampaTabellina(t)
    print("ricomincia!")
