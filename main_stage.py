import pygame

from background import Background
from text_sprite import TextSprite
from pygame.sprite import Group

class MainStage(Group):

    app = None

    def __init__(self, game):
        Group.__init__(self)

        self.game = game

        self.bg = Background(game)
        self.add(self.bg)

        self.title_text = TextSprite("SEGA MASTER SYSTEM", game.assets["TITLE_FONT"])
        (self.title_text.x, self.title_text.y) = (455,70)
        self.title_text.centered = True

    #end of init

    def update(self, dt):
        Group.update(self, dt)

        pass

    #end of update

    def draw(self, renderer):
        Group.draw(self, renderer)

        #self.bg.draw(renderer)
        self.title_text.draw(renderer)

    #end of draw

#end of MainStage