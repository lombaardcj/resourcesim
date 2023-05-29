import threading
import logging
import sys
import time

# import pygame
import pygame
from pygame.locals import *

# import local modules
from gameengine import GameState
engine = GameState(startup_tick_duraction=1)

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

# initialise the logger
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
log = logging.getLogger(__name__)
log.info("Initialising logger")

# initialize pygame
pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 20)

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FG = WHITE
BG = BLACK
    
# Screen information
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# create the display surface object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")
# pygame.mouse.set_visible(False)

crosshair = Crosshair("assets/images/target.png")

camera_group = pygame.sprite.Group()
camera_group.add(crosshair)

def loop():
    while True:
        engine.process()
        
        # check for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # draw the game
        screen.fill(BLACK)
        
        # # print the fps to the surface       
        # text = font.render("Tick: " + str(int(engine.get_tick())), True, FG)
        # screen.blit(text, (100, 0))
        
        # # print the flag stack to the surface
        # # loop through each flag and also get the index
        for index, flag in enumerate(engine.get_flag_stack()):
        #     text = font.render(str(flag), True, FG)
        #     screen.blit(text, (0, 20 + 20 * index))
            
            # translate the flag location to the screen
            pygame.draw.circle(screen, BLUE, (int(flag.location.x*10), int(flag.location.y*10)), 5)
        
        # for path_link in engine.get_path_link_stack():
        #     pygame.draw.line(screen, WHITE, 
        #         (int(path_link.flagA.location.x*10), int(path_link.flagA.location.y*10)),
        #         (int(path_link.flagB.location.x*10), int(path_link.flagB.location.y*10)),
        #     1)
        
        camera_group.update()
        camera_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)

        # sleep for the tick duration
        # time.sleep(engine.get_tick_duration())

if __name__ == "__main__":
    t = threading.Thread(target=loop)
    t.start()
    t.join()