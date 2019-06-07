import pygame
from random import randint, choice

SCREEN_SIZE = (640, 480)
TILE_SIZE = 30
DIRECTIONS = ("up", "down", "left", "right")

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

done = False

clock = pygame.time.Clock()

class Entity:
  def __init__(self, x, y, color, level):
    self.x = x
    self.y = y
    self.w = TILE_SIZE
    self.h = TILE_SIZE
    self.level = level
    self.color = color

  def update(self):
    pass

  def collide(self, entity):
    return False

  def draw(self): 
    pygame.draw.rect(screen, self.color, pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, self.w, self.h))

  def move(self, direction):
    next_x = self.x
    next_y = self.y

    if direction == "up":
      if self.y > 0:
        next_y -= 1
      else:
        next_y = self.level.h - 1
    elif direction == "down":
      if self.y < self.level.h - 1:
        next_y += 1
      else:
        next_y = 0
    elif direction == "left":
      if self.x > 0:
        next_x -= 1
      else:
        next_x = self.level.w - 1
    elif direction == "right":
      if self.x < self.level.w - 1:
        next_x += 1
      else:
        next_x = 0

    e = self.level.get_entity_at_coords(next_x, next_y)
    if e == None or self.collide(e) == True:
      self.x = next_x
      self.y = next_y


class Player(Entity):
  def __init__(self, x, y, level):
    super().__init__(x, y, (0, 255, 0), level)

  def move(self, direction):
    self.level.can_move = True
    super().move(direction)

  def collide(self, entity):
    if isinstance(entity, Collectible):
      self.level.entities.remove(entity)
      self.level.score += 1

      if self.level.score == self.level.max_score:
        self.level.won = True

      return True

    elif isinstance(entity, Enemy):
      self.level.entities.remove(entity)
      self.level.kills += 1
      return False


class Enemy(Entity):
  def __init__(self, x, y, level):
    super().__init__(x, y, (255, 0, 0), level)

  def collide(self, entity):
    if isinstance(entity, Collectible):
      return True
    elif isinstance(entity, Player):
      self.level.entities.remove(entity)
      self.level.game_over = True
      return True


  def update(self):
    if self.level.can_move:
      self.move(choice(DIRECTIONS)) 


class Obstacle(Entity):
  def __init__(self, x, y, level):
    super().__init__(x, y, (0, 255, 255), level)


class Collectible(Entity):
  def __init__(self, x, y, level):
    super().__init__(x, y, (255, 255, 0), level)


class Level:
  def __init__(self, w, h, number_of_monsters, number_of_collectibles, number_of_obstacles, player_x = 0, player_y = 0):
    self.w = w
    self.h = h
    self.player = player = Player(player_x, player_y, self)
    self.entities = [player]
    self.score = 0
    self.kills = 0
    self.max_score = number_of_collectibles
    self.won = False
    self.game_over = False
    self.can_move = False

    count = 0
    while number_of_monsters >= count:
      x = randint(0, self.w - 1)
      y = randint(0, self.h - 1)
      if self.get_entity_at_coords(x, y) == None:
        self.entities.append(Enemy(x, y, self))
        count += 1

    count = 0
    while number_of_collectibles >= count:
      x = randint(0, self.w - 1)
      y = randint(0, self.h - 1)
      if self.get_entity_at_coords(x, y) == None:
        self.entities.append(Collectible(x, y, self))
        count += 1
    
    count = 0
    while number_of_obstacles >= count:
      x = randint(0, self.w - 1)
      y = randint(0, self.h - 1)
      if self.get_entity_at_coords(x, y) == None:
        self.entities.append(Obstacle(x, y, self))
        count += 1

  def get_entity_at_coords(self, x, y):
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

  def update(self):
    for e in self.entities:
      e.update()

    self.can_move = False

  def draw(self):
    pygame.draw.rect(
      screen,
      (255, 255, 255),
      pygame.Rect(0, 0, *SCREEN_SIZE)
    )

    # print("SCORE: {}".format(self.score))
    # print("KILLS: {}".format(self.kills))

    for e in self.entities:
      e.draw()


levels = [
  Level(3, 3, 1, 1, 1, 1, 1),
  Level(5, 5, 3, 2, 5, 3, 3),
  Level(10, 10, 6, 3, 20, 5, 5),
]

current_level_index = 0

while not done:
  current_level = levels[current_level_index]
  current_level.draw()

  if current_level.won:
    current_level_index += 1
    if current_level_index == len(levels):
      #print("hai vinto!")
      done = True
    else:
      current_level = levels[current_level_index]

  if current_level.game_over:
    # print("LOOOOOOOOOOOOOOOOOSER!")
    done = True

  player = current_level.player

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player.move("left")
      elif event.key == pygame.K_RIGHT:
        player.move("right")
      elif event.key == pygame.K_UP:
        player.move("up")
      elif event.key == pygame.K_DOWN:
        player.move("down")

  pygame.display.flip()

  current_level.update()
  clock.tick(60)
