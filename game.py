
# pylint: disable=no-member

import pygame
import sys
from background import Background

ASSETS =  {
    "BG":"./src/bg.jpg",
    "GRAD_BG":"./src/grad_bg.png"
}

class Game(object):
    def __init__(self, app):
        self.app = app
        self.assets = ASSETS

        self.size = [
            app.config.getint("DISPLAY", "width"),
            app.config.getint("DISPLAY", "height")
        ]

        flags = 0
        if app.config.getboolean("DISPLAY", "fullscreen"):
             flags = pygame.FULLSCREEN

        self.renderer = pygame.display.set_mode(self.size, flags)
    
    #end of init

    ''' 
    Game start method
    '''
    def start(self):
        self.bg = Background(self)

    #end off start

    '''
    Game update method
    '''
    def update(self, dt):
        pass
    
    #end of update

    ''' 
    Game render method
    '''
    def render(self):
        self.bg.draw(self.renderer)
        pygame.display.flip()
    
    #end of render

#end of Game