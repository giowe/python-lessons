import pygame
from random import randint

def getRandomColor():
  return (randint(0, 255), randint(0, 255), randint(0, 255))

SCREEN = (600, 400)

pygame.init()
screen = pygame.display.set_mode(SCREEN)

done = False

class Entity():
  def __init__(self):
    self.x = randint(100, 200)
    self.y = randint(100, 200)
    self.h = 2
    self.w = 2

    self.speed_x = randint(2, 10)
    self.speed_y = randint(2, 10)
    self.color = getRandomColor()

  def move(self):
    self.x += self.speed_x
    self.y += self.speed_y

    if self.x + self.w >= SCREEN[0] or self.x <= 0:
      self.speed_x *= -1
      self.color = getRandomColor()

    if self.y + self.h >= SCREEN[1] or self.y <= 0:
      self.speed_y *= -1
      self.color = getRandomColor()

  def draw(self):
    pygame.draw.rect(
      screen, 
      self.color,
      (self.x, self.y, self.w, self.h)
    )


clock = pygame.time.Clock()

entities = []
for i in range(100):
  entities.append(Entity())

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  '''
  pygame.draw.rect(
    screen, 
    (0, 0, 0),
    (0, 0, SCREEN[0], SCREEN[1])
  )
  '''

  for e in entities:
      e.draw()
      e.move()

  pygame.display.flip()
  clock.tick(60)
