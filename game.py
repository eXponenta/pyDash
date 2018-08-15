
# pylint: disable=no-member

import pygame
import sys
from main_stage import MainStage

ASSETS =  {
    "BG_FULL":"./src/bg_full.jpg",
    "LOGO": "./src/logo.png",

    "TITLE_FONT": "./src/fonts/MagistralBlackC.otf",
}

class Game(object):

    current_stage = None
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
        self.main_stage = MainStage(self)

        self.current_stage = self.main_stage
    #end off start

    '''
    Game update method
    '''
    def update(self, dt):
        if(self.current_stage != None):
            self.current_stage.update(dt)

    
    #end of update

    ''' 
    Game render method
    '''
    def render(self):
        
        if(self.current_stage != None):
            self.current_stage.draw(self.renderer)

        pygame.display.flip()
    
    #end of render

#end of Game