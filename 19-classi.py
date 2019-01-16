#---------------------------------------
class Persona:
  def __init__(self, nome, cognome, anni):
    self.nome = nome
    self.cognome = cognome
    self.anni = anni

  def compleanno(self):
    self.anni += 1

  def saluta(self, nome):
    return "ciao " + nome + " io sono " + self.nome + " " + self.cognome

  def __str__(self):
    return "io sono " + self.nome + " " + self.cognome

  def __int__(self):
    return self.anni

#---------------------------------------

class Studente(Persona):
  def __init__(self, nome, cognome, anni, scuola):
    Persona.__init__(self, nome, cognome, None)
    self.scuola = scuola

  def saluta(self, nome):
    return Persona.saluta(self, nome) + " sono iscritto nella scuola di nome " + self.scuola 

  def __str__(self):
    return Persona.__str__(self) + " " + self.scuola

#---------------------------------------
p = Persona("Giovanni", "Bruno", 31)
s = Studente("Giovanni", "Bruno", 31, "Classico")

print(p.saluta("x"))
print(s.saluta("x"))