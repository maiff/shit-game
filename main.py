background_image_filename = './images/mainBg.jpg'
all1 = './images/sltq1.png'
all2 = './images/sltq0.png'
mappic = './images/map.png'
_ = './music'
music = [_+'/go.mp3',_+'/bg.mp3']
import pygame
from pygame.locals import *
from sys import exit
from util import *
import random

pygame.init()
screen_size  = (550,970)
screen = pygame.display.set_mode(screen_size, 0, 32)

Fullscreen = False

background = pygame.image.load(background_image_filename).convert_alpha()
background = pygame.transform.scale(background,screen_size)
title = cropimg(all1, ( 335, 628,955,960))
title= pygame.transform.scale(title,(550,300)).convert_alpha()

bling= cropimg(all1, ( 45, 673,298,917))
fontMain= cropimg(all2, ( 653, 134,932,309))
toppic= cropimg(mappic, ( 0, 0,717,729))
toppic= pygame.transform.scale(toppic,(550,600)).convert_alpha()
bottompic= cropimg(mappic, ( 0, 512,717,729))
bottompic= pygame.transform.scale(bottompic,(550,470)).convert_alpha()


# bling= pygame.transform.scale(img,(550,300)).convert_alpha()


def init(screen, start, ty):
     # background
    if not start:
      ##################todo#########################
      screen.blit(background, (0,0))
      background.blit(title, (0,0))
      background.blit(fontMain, (150,650))
      ##################todo#########################

    else:
      screen.blit(bottompic, (0,0))
      screen.blit(bottompic, (0,300))
      screen.blit(bottompic, (0,600))
      screen.blit(toppic, (0,ty))
      screen.blit(bottompic, (0,512))

class Shit():
  def __init__(self, screen):
    self.shit= cropimg(all2, ( 298, 456,381,540))
    self.screen = screen
    self.x = 251
    self.y = 137-96

  def draw(self):
    ##################todo#########################
    self.screen.blit(self.shit, (self.x, self.y))
    ##################todo#########################
  
  def update(self):
    ##################todo#########################
    posx, posy = pygame.mouse.get_pos()
    if self.y >= 500:
      if posx <= 83:
        posx = 83
      if posx >= 384:
        posx = 384
      self.x = posx
      self.y = 500
    else:
      self.y += 10
    return self.y
    ##################todo#########################

def gettime(screen, clock, sum_time):
  font = pygame.font.SysFont("arial", 40)
  time_passed = clock.tick()
  time_passed_seconds = time_passed / 1000.0
  sum_time += time_passed_seconds
  text_surface = font.render(str(sum_time)[:4], True, (255, 255, 255))
  screen.blit(text_surface, (0, 0))
  return sum_time

class Hole (pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        self.hole= cropimg(all2, (643, 0,773,133))
        self.hx = random.randint(83, 384)
        self.hy = 970
        self.__isInGroup = False
    def draw(self):
        
        ##################todo#########################
        ##################todo#########################
    def update(self):
        ##################todo#########################
        ##################todo#########################

        
    def add (self, group):
        
        group.append(self)
        self.__isInGroup = True
    def remove(self, group):
        
        group.remove(self)
        self.__isInGroup = False
    def alive(self):
        
        return self.__isInGroup

    def collide(self, ball):
        w = 381 - 298
        h = 540 - 456

        x = shit.x
        y = shit.y

        holeW = 773 - 643
        holwH = 133


        x1, y1 = x, y
        x2, y2 = x + w, y
        x3, y3 = x, y+h
        x4, y4 = x+w, y+h

        if (x1>= self.hx and x1 <= self.hx+holeW and y1>= self.hy and y1 <= self.hy+holwH) or \
          (x2>= self.hx and x2 <= self.hx+holeW and y2>= self.hy and y2 <= self.hy+holwH) or \
          (x3>= self.hx and x3 <= self.hx+holeW and y3>= self.hy and y3 <= self.hy+holwH) or \
          (x4>= self.hx and x4 <= self.hx+holeW and y4>= self.hy and y4 <= self.hy+holwH):
            return True
        
        return False



    
def main():
  global screen
  pygame.mixer.music.load( music[0] ) 

  start = False
  
  ty= 0
  playing = False
  
  clock = pygame.time.Clock()
  sum_time = 0
  preTime = 0
  gameover = False

  hole_XS = []

  ss = Shit(screen)
  
  while 1:
    
    for event in pygame.event.get():
      if event.type == QUIT:
              exit()
    
      if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(screen_size, FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(screen_size, 0, 32)
      if event.type == pygame.MOUSEBUTTONDOWN:
        if not start:
          pygame.mixer.music.play()

          start = True
          playing = True
          screen.fill((0,0,0))
          
    init(screen, start, ty)
    posx, posy = pygame.mouse.get_pos()
    if start:
      ##################todo#########################
     
      ##################todo#########################

      if y >= 500:
        ty -= 10
        if playing:
          pygame.mixer.music.load( music[1] ) 
          pygame.mixer.music.play()
          playing = False

        if not gameover:
          sum_time = gettime(screen, clock, sum_time)

        
        if int(sum_time) % 2 == 0 and int(sum_time) != preTime:
          ##################todo#########################

          
          ##################todo#########################

        for h in (hole_XS):
          ##################todo#########################

         
          ##################todo#########################

        
        for h in hole_XS:
          iscollide = h.collide(ss)
          if iscollide:
            gameover = True
   

      if gameover:
        main()
      
    pygame.display.update()



main()