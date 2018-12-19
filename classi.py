class Persona:
  def __init__(self, nome):
    self.nome = nome

  def saluta(self):
    print("sono una persona e mi chiamo", self.nome)

p1 = Persona("Giovanni")
p1.nome = "Paolo"
p1.saluta()
