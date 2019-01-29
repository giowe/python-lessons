from random import randint, choice
import os
import pygame

DIRECTIONS = "w", "a", "s", "d"
SCREEN_SIZE = (800, 600)
FONT = "./Amatic-Bold.ttf"

class Tilemap():
  def __init__(self, image_path, tile_size, padding, offset = (0, 0)):
    self.palette = pygame.image.load(image_path)
    self.tile_size = tile_size
    self.padding = padding
    self.offset = offset
  
  def cut_n_draw(self, surface, tile_coords, surface_coords):
    x = self.offset[0] + (tile_coords[0] * (self.tile_size[0] + self.padding[0]))
    y = self.offset[1] + (tile_coords[1] * (self.tile_size[1] + self.padding[1]))
    surface.blit(self.palette, surface_coords, pygame.Rect(x, y, *self.tile_size))

class Game():
  def __init__(self):
    pygame.init()
    self.tilemap = Tilemap("tilemap.jpg", (30, 30), (3, 3), (2, 2))

    self.screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('gioco')
    self.font = pygame.font.Font(FONT, 100)
    self.game_over_flag = False
    self.win_flag = False

    self.levels = []
    for level_index in range(11):
      self.levels.append(World(level_index+1, self))

    self.current_level_index = 0

  def get_current_level(self):
    return self.levels[self.current_level_index]

  def get_player(self):
    return self.get_current_level().player

  def is_game_running(self):
    return self.game_over_flag == False and self.win_flag == False

  def game_over(self):
    self.game_over_flag = True

  def win(self):
    if self.current_level_index >= len(self.levels) -1:
      self.win_flag = True
    else:
      self.current_level_index += 1

  def draw(self):
    level = self.get_current_level() 
    
    for x in range(SCREEN_SIZE[0]//self.tilemap.tile_size[0]+1):
      for y in range(SCREEN_SIZE[1]//self.tilemap.tile_size[1]+1):
        self.tilemap.cut_n_draw(self.screen, (3, 3), (x * 30, y * 30))

    level.draw()

    if self.win_flag:
      text = self.font.render("A WINNER IS YOU!", True, (0, 255, 0))
      w, h = text.get_size()
      self.screen.blit(text, ((SCREEN_SIZE[0] - w) / 2, (SCREEN_SIZE[1] - h) / 2))
    elif self.game_over_flag:
      text = self.font.render("WASTED!", True, (255, 0, 0))
      w, h = text.get_size()
      self.screen.blit(text, ((SCREEN_SIZE[0] - w) / 2, (SCREEN_SIZE[1] - h) / 2))

    pygame.display.update()
  
  def draw_terminal(self):
    os.system("clear")
    level = self.get_current_level()  
    print("---------------------------------------------")
    print("LEVEL {}".format(self.current_level_index + 1))
    print("---------------------------------------------")
    print(level)

    if self.game_over_flag:
      print("LOOOOSER")
    elif self.win_flag:
      print("A WINNER IS YOU")
  

  def update(self):
    if self.is_game_running():
      self.get_current_level().update()

class World():
  def __init__(self, level_name, game):
    self.game = game
    self.entities = []
    self.player = None
    self.gold = None 
    
    f = open("./levels/{}.br1".format(level_name))
    rows = f.readlines()
    f.close()

    self.h = len(rows)
    self.w = len(rows[0])-1

    tilemap = self.game.tilemap
  
    background = pygame.Surface((self.w * tilemap.tile_size[0], self.h * tilemap.tile_size[1]))
    self.layers = [background]

    for y in range(len(rows)):
      r = rows[y].replace("\n", "")
      for x in range(len(r)):
        #GENERATING BACKGROUND
        tilemap.cut_n_draw(background, choice([(4, 2), (5, 2), (6, 2)]), (x * tilemap.tile_size[0], y * tilemap.tile_size[1]))

        #MAP PARSING
        char = r[x]
        if char == "#":
          self.entities.append(Wall(x, y, self))
        elif char == "@":
          if self.player is None:
            self.player = Player(x, y, self)
            self.entities.append(self.player)
          else:
            raise Exception("Il player è già presente nel livello {}".format(level_name))
        elif char == ">":
          self.entities.append(Monster(x, y, self))
        elif char == "o":
          if self.gold is None:
            self.gold = Gold(x, y, self)
            self.entities.append(self.gold)
          else:
            raise Exception("Il gold è già presente nel livello {}".format(level_name))

    if self.player is None:
      raise Exception("Il player non è presente nel livello {}".format(level_name))
    if self.gold is None:
      raise Exception("Il gold non è presente nel livello {}".format(level_name))

  def update(self):
    for e in self.entities:
      e.update()

  def _get_random_coords(self):
    return (randint(0, self.w -1), randint(0, self.h -1))

  def get_entity(self, x, y):
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

  def draw(self):
    for layer in self.layers:
      self.game.screen.blit(layer, (0, 0))

    entities2Draw = self.entities[:]
    for row in range(self.h):
      for col in range(self.w):
        for e in entities2Draw:
          if e.x == col and e.y == row:
            e.draw()
            entities2Draw.remove(e)
            break

  def __str__(self):
    out=""
    entities2Draw = self.entities[:]
    for row in range(self.h):
      for col in range(self.w):
        for e in entities2Draw:
          if e.x == col and e.y == row:
            out+="[{}]".format(e)
            entities2Draw.remove(e)
            break
        else:
          out+="[ ]"

      out+="\n"
    return out

class Entity():
  def __init__(self, x, y, world, graphic, tile_graphic):
    self.x = x
    self.y = y
    self.graphic = graphic
    self.tile_graphic = choice(tile_graphic)
    self.world = world

  def move(self, direction=None):
    if direction is None:
      direction = choice(DIRECTIONS)

    future_x = self.x
    future_y = self.y

    if direction == "w":
      if self.y > 0:
        future_y -= 1
    elif direction == "s":
      if self.y < self.world.h-1:
        future_y += 1
    elif direction == "a":
      if self.x > 0:
        future_x -= 1
    elif direction == "d":
      if self.x < self.world.w-1:
        future_x += 1
    else:
      raise Exception("comando non valido, le direzioni accettate sono 'w' 'a' 's' 'd'")

    e = self.world.get_entity(future_x, future_y)
    if e is None:
      self.x = future_x
      self.y = future_y
    else:
      self.collide(e)

  def collide(self, entity):
    self_class = self.__class__.__name__
    entity_class = entity.__class__.__name__
    
    if self_class == "Player":
      if entity_class == "Monster":
        self.world.game.game_over()
      elif entity_class == "Gold":
        self.world.game.win()
    elif self_class == "Monster":
      if entity_class == "Player":
        self.world.game.game_over()
  
  def update(self):
    return None

  def draw(self):
    tile_w, tile_h = self.world.game.tilemap.tile_size
    self.world.game.tilemap.cut_n_draw(
      self.world.game.screen,
      self.tile_graphic,
      (self.x * tile_w, self.y * tile_h)
    )
    '''
    pygame.draw.rect(
      self.world.game.screen, 
      self.color,
       pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
    )
    '''

  def __str__(self):
    return self.graphic

class Player(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "@", [(2, 3)])

class Wall(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "#", [(13, 1), (14, 1)]) 

class Monster(Entity):
  def __init__(self, x, y, world):
    #Entity.__init__(self, x, y, "M")
    super().__init__(x, y, world, ">", [(0, 1)])

  def update(self):
    self.move()

class Gold(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "o", [(1, 3)])

  def update(self):
    if self.graphic == "O":
      self.graphic = "o"
    else:
      self.graphic = "O"


game = Game()
clock = pygame.time.Clock()
crashed = False

while not crashed:
    player = game.get_player()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
          if game.is_game_running():
            if event.key == pygame.K_LEFT:
              player.move("a")
            elif event.key == pygame.K_RIGHT:
              player.move("d")
            elif event.key == pygame.K_UP: 
              player.move("w")
            elif event.key == pygame.K_DOWN:
              player.move("s")
            elif event.key == pygame.K_n:
              game.win()

          game.update()
    game.draw()
    clock.tick(30)