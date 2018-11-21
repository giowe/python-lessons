#---------------------------------------
class Persona:
  def __init__(self, nome, cognome, anni):
    self.nome = nome
    self.cognome = cognome
    self.anni = anni

  def saluta(self, nome):
    return "ciao " + nome + " io sono " + self.nome + " " + self.cognome

  def __str__(self):
    return "io sono " + self.nome + " " + self.cognome

  def __int__(self):
    return self.anni

#---------------------------------------

class Studente(Persona):
  def __init__(self, nome, cognome, anni, scuola):
    Persona.__init__(self, nome, cognome, anni)
    self.scuola = scuola

  def saluta(self, nome):
    return Persona.saluta(self, nome) + " e sono iscritto nella scuola di nome " + self.scuola 

  def __str__(self):
    return Persona.__str__(self) + " " + self.scuola

#---------------------------------------
p = Persona("Giovanni", "Bruno", 31)
s = Studente("Tizio", "Caio", 31, "Spalla")

print(p.saluta("Y"))
print(s.saluta("X"))
