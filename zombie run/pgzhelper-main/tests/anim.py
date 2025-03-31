import pgzrun
from pgzhelper import *
from anim_oop import Test

alien = Actor('alien_walk1')
alien.images = ['alien_walk1', 'alien_walk2']
alien.fps = 3

alien2 = Actor('alien_walk1')
alien2.load_images('alien_walk_spritesheet', 2, 1, subrect=(0, 0, 134, 96))
alien2.fps = 5
alien2.topleft = 100, 0

test = Test()

def update():
  alien.animate()
  alien2.animate()
  test.move()

def draw():
  game.exit()
  screen.clear()
  alien.draw()
  alien2.draw()
  
pgzrun.go()