
# pylint: disable=no-member

import pygame
import sys
from main_stage import MainStage

ASSETS =  {
    "BG_FULL":"./src/bg_full.jpg",
    "LOGO": "./src/logo.png",

    "TITLE_FONT": "./src/fonts/MagistralBlackC.otf",
    "LIST_FONT":"./src/fonts/BebasNeue Regular.otf",

    "ICONS":[
        {"title":"ИЗБРАННОЕ", "img":"./src/icons/fav_{0}.png"}, #favorites
        {"title":"SEGA GENESIS", "img":"./src/icons/gen_{0}.png"}, #sega gen
        {"title":"SEGA MASTER SYSTEM", "img":"./src/icons/sms_{0}.png"}, #sms
        {"title":"NES", "img":"./src/icons/nes_{0}.png"}, #nes
        {"title":"SNES", "img":"./src/icons/snes_{0}.png"}, #snes
        {"title":"SD CARD", "img":"./src/icons/sdcard_{0}.png"}, #sdcard
        {"title":"НАСТРОЙКИ", "img":"./src/icons/opt_{0}.png"}, #config
    ],

    "SELECTOR": "./src/icons/border.png"
}

class Game(object):

    current_stage = None
    def __init__(self, app):
        self.app = app
        self.assets = ASSETS

        self.size = [
            720,#app.config.getint("DISPLAY", "width"),
            576 #app.config.getint("DISPLAY", "height")
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