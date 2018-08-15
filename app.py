#! /usr/bin/python3
# pylint: disable=no-member

import sys
import configparser
import pygame
import os

from game import Game

#force freetype
os.environ['PYGAME_FREETYPE'] = '1'

'''
Base App class
'''

class App(object):
    
    def __init__(self):
        
        self.config = configparser.ConfigParser()
        self._lastTick = 0
        self.deltaTime = 0

        try:
            self.config.readfp(open('config.cfg'))
        except:
            self.config['DISPLAY'] = {'width':'720', 'height':'576', 'fullscreen':'false'}
            self.config.write(open('config.cfg', 'w'))
        
        pygame.init()
        self.game = Game(self)
    
    #end of init

    def run(self):
        
        self.game.start() # start game 
        self.game.active = True

        self._lastTick = pygame.time.get_ticks()
        
        while 1: # main game loop
            
            # deltaTime in seconds.
            t = pygame.time.get_ticks()
            self.deltaTime = (t - self._lastTick) / 1000.0
            self._lastTick = t
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.game.active = False
                    sys.exit(0)
                
            self.game.update(self.deltaTime)
            self.game.render()
    
    #end of run

#end of App