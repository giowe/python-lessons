#---------------------------------------
class Persona:
  def __init__(self, nome, cognome, anni):
    self.nome = nome
    self.cognome = cognome
    self.anni = anni

  def saluta(self, nome):
    return "ciao {} mi chiamo {} {} e ho {} anni".format(nome, self.nome, self.cognome, self.anni)

  def __str__(self):
    return "<{} {} {} {}>".format(self.__class__.__name__, self.nome, self.cognome, self.anni)

  def __int__(self):
    return self.anni
  
#---------------------------------------

class Studente(Persona):
  def __init__(self, nome, cognome, anni, scuola):
    Persona.__init__(self, nome, cognome, anni)
    self.scuola = scuola

  def fai_verifica(self, materia):
    print("sto facendo una verifica di {}".format(materia))

  def saluta(self, nome):
    return "{} e faccio la scuola chiamata {}".format(Persona.saluta(self, nome), self.scuola)
 
#---------------------------------------
p = Persona("Giovanni", "Bruno", 31)
s = Studente("Tizio", "Caio", 31, "Spalla")


print(p)
print(s)