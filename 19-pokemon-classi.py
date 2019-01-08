class Monster:
  def __init__(self, name, hp, damage, armor):
    self.name = name
    self.max_hp = hp
    self.cur_hp = hp
    self.damage = damage
    self.armor = armor
    self.level = 1

  def status(self):
    status = "name: {}\nlevel:{}\nhp: {}/{}".format(self.name, self.level, self.cur_hp, self.max_hp)
    if self.cur_hp <= 0:
      status += " MORTO"
    print(status)

  def attack(self, target):
    if self.cur_hp <= 0:
      print("da morto non ce la puoi proprio fare...")
      return
    
    if target.cur_hp <= 0:
      print("non puoi infierire sul corpo del povero {}".format(target.name))
      return

    damage = self.damage - target.armor
    target.cur_hp -= damage

    if target.cur_hp < 0:
      target.cur_hp = 0

    log = "{} attacca {}\nvengono inflitti {} danni".format(self.name, target.name, damage)
    print(log)
    target.status()

