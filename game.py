
# pylint: disable=no-member
from app import App
import pygame
import sys

class Game(App):
    def __init__(self):
        App.__init__(self)        
        pygame.init()
        pygame.display.init()
        
        self.size = [
            self.config.getint("DISPLAY", "width"),
            self.config.getint("DISPLAY", "height")
        ]

        flags = 0
        if self.config.getboolean("DISPLAY", "fullscreen"):
             flags = pygame.FULLSCREEN

        self.renderer = pygame.display.set_mode(self.size, flags)
        self.start()
    
    ''' 
    Game start method
    '''
    def start(self):
        self.active = True

        pass
    '''
    Game update method
    '''
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.active = False
                sys.exit(0)
        
        #render after update 
        self.render()

    ''' 
    Game render method
    '''
    def render(self):
        pygame.display.flip()