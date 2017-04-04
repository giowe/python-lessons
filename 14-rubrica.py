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
  pass

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
	pass

seeder(100)
print_contact(2)