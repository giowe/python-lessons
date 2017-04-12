from random import randint

rubrica = []

def add_padding(text, padding = 20):
	for i in range(padding - len(text)):
		text += ' '
	return text

def add_contact(first_name, last_name, phone):
	global rubrica
	rubrica.append([first_name, last_name, phone])

def remove_contact(first_name, last_name):
  global rubrica
  for contatto in rubrica:
    if contatto[0] == first_name and contatto[1] == last_name:
      rubrica.remove(contatto)
      return contatto

  return None

nomi = ['Tizio', 'Caio', 'Sempronio', 'Proserpina', 'Letizia']
congomi = ['Rossi', 'Verdi', 'Bianchi', 'Azzurro', 'Rosi']
def seeder(number):
  global nomi, cognomi
  for i in range(number):
    nome = nomi[randint(0, len(nomi)-1)]
    cognome = congomi[randint(0, len(congomi)-1)]
    telefono = ''
    for n in range(10):
      telefono += str(randint(0,9))

    add_contact(nome, cognome, telefono)

def print_contact(index):
	global rubrica
	contact = rubrica[index]
	print(index+1, add_padding(contact[0]), add_padding(contact[1]), add_padding(contact[2]))

def print_rubrica(skip, limit):
  for i in range(skip, skip+limit):
    print_contact(i)

seeder(100)
print_rubrica(0, 100)
print('Ora eliminiamo un contatto')
nome = input('Come si chiama il contatto che vuoi eliminare? ')
cognome = input('Qual è il cognome della persona da eliminare? ')
eliminato = remove_contact(nome, cognome)
if eliminato != None:
  print('Hai eliminato il contatto', eliminato[0], eliminato[1], eliminato[2])
else:
  print('Non ho trovato nessun contatto che si chiami', nome, cognome)  