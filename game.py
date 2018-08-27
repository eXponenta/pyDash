
# pylint: disable=no-member

import pygame
import sys
from main_stage import MainStage
from text_sprite import TextSprite

ASSETS = {
    "BG_FULL": "./src/bg_full.jpg",
    "LOGO": "./src/logo.png",

    "TITLE_FONT": "./src/fonts/MagistralBlackC.otf",
    "LIST_FONT": "./src/fonts/BebasNeue Regular.otf",

    "ICONS": [
        {"title": u"ИЗБРАННОЕ", "img": "./src/icons/fav_{0}.png"},  # favorites
        {"title": "SEGA GENESIS", "img": "./src/icons/gen_{0}.png"},  # sega gen
        {"title": "SEGA MASTER SYSTEM", "img": "./src/icons/sms_{0}.png"},  # sms
        {"title": "NES", "img": "./src/icons/nes_{0}.png"},  # nes
        {"title": "SNES", "img": "./src/icons/snes_{0}.png"},  # snes
        {"title": "SD CARD", "img": "./src/icons/sdcard_{0}.png"},  # sdcard
        {"title": u"НАСТРОЙКИ", "img": "./src/icons/opt_{0}.png"},  # config
    ],

    "SELECTOR": "./src/icons/border.png"
}


class Game(object):

    current_stage = None

    def __init__(self, app):

        self.app = app
        self.assets = ASSETS

        self.fps_text = TextSprite("fps:00", None, 14)
        self.count = 0
        self.avg_fps = 0

        self.size = [
            720,  # app.config.getint("DISPLAY", "width"),
            576  # app.config.getint("DISPLAY", "height")
        ]

        flags = 0

        if app.config.getboolean("DISPLAY", "fullscreen"):
            flags = pygame.FULLSCREEN

        _tryogl = app.config.getboolean("DISPLAY", "opengl") and pygame.OPENGL

        near = [0, 0]

        # try get hardware asselerated
        _testFlags = flags | pygame.HWSURFACE | _tryogl | pygame.DOUBLEBUF
        _modes = pygame.display.list_modes(32, _testFlags)

        if (_modes != -1 and len(_modes) == 0):
            _modes = pygame.display.list_modes(32, flags)
            #_testFlags = flags

        if (_modes == -1):
            _modes = [self.size]
            #flags = _testFlags

        _nears = [m for m in _modes[::-1] if m[0] >=
                  self.size[0] and m[1] >= self.size[1]]

        if(len(_nears) > 0):
            near = _nears[0]
        try:
            self.virtual_render = pygame.display.set_mode(near, _testFlags, 32)
            print("[MODE] OPENGL (%s), HW (%s), RES: %s" %
                  (_tryogl and 1, (flags & pygame.HWSURFACE), near))
        except Exception as e:
            print("[MODE] Error: \n %s" % e)
            self.virtual_render = pygame.display.set_mode((0, 0), flags)

        self.renderer = pygame.surface.Surface(self.size)

        print('render info:' + str(pygame.display.Info()))

    # end of init

    ''' 
    Game start method
    '''

    def start(self):
        self.main_stage = MainStage(self)

        self.current_stage = self.main_stage
    # end off start

    '''
    Game update method
    '''

    def update(self, dt):
        if(self.current_stage != None):
            self.current_stage.update(dt)

        if(dt == 0):
            return

        if(self.count < 0.5):
            self.count += dt
            self.avg_fps = 0.5 * (self.avg_fps + 1 / dt)
        else:
            self.fps_text.set_text("avg fps: %d" % self.avg_fps)
            self.count = 0

    # end of update

    ''' 
    Game render method
    '''

    def render(self):

        _flip = False
        if(self.current_stage != None):
            _flip = self.current_stage.draw(self.renderer)

        if(_flip):
            size = [self.virtual_render.get_width(), self.virtual_render.get_height()]
            pygame.transform.scale(self.renderer, size, self.virtual_render)
            pygame.display.flip()

    # end of render

# end of Game
