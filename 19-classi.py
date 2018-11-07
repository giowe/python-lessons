class Persona:
  def __init__(self, nome):
    self.nome = nome

  def saluta(self):
    print("ciao, sono", self.nome)

p = Persona("Pino")
p2 = Persona("Caio")

p.saluta()
p2.saluta()

if p.nome == "Giovanni":
  print("ciao padrone")
  