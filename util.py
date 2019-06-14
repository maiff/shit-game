import pygame
from pygame.locals import *

def cropimg(image, region):
    x1,y1,x2,y2 = region
    buttonStates = pygame.image.load(image).convert_alpha()
    print(region[2:])
    cropped = pygame.Surface((x2-x1, y2-y1), flags=SRCALPHA)
    cropped.blit(buttonStates, (0, 0), (x1,y1,x2-x1, y2-y1))
    return cropped