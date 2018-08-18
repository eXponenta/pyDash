from sprite import Sprite

class ImageButton(Sprite):

    NORMAL = 0
    SELECTED = 1
    DISABLED = 2

    def __init__(self, imgs):
    
        Sprite.__init__(self, imgs[0])

        self.__state = -1
        self.__states = list()

        self.__states = imgs
        

        self.state = ImageButton.NORMAL

    #end of init

    def update(self, dt):
    
        Sprite.update(self, dt)
    
    #end of update

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, state):
        self.__state = state
        
        if state < len(self.__states):
            self.image = self.__states[state]
        else:
            self.image = self.__states[ImageButton.NORMAL]
        
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        
    

#end of ImageButton