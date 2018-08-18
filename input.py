import pygame
# pylint: disable=no-member


class Input(object):
    
    EVENT_UP = "up"
    EVENT_DOWN = "down"
    EVENT_NEXT = "enter"
    EVENT_BACK = "back"

    EVENT_2_KEYS = {
        EVENT_UP: [pygame.K_UP],
        EVENT_DOWN: [pygame.K_DOWN],
        EVENT_NEXT: [pygame.K_RETURN, pygame.K_SPACE],
        EVENT_BACK: [pygame.K_ESCAPE]
    }

    def __init__(self):
        
        self.__envents = dict()

        pass
    
    def collectEvents(self, event):
        _ext_type = None
        
        if(event.type == pygame.KEYDOWN):
            for key in Input.EVENT_2_KEYS:
                if(event.key in Input.EVENT_2_KEYS[key]):
                    _ext_type = key
                    break
        
        if(_ext_type  == None): return

        #try:
        for _e in self.__envents[_ext_type]:
            _e()
        #    print(_e)
        #except:
        #    print("Error execute method")
        #    pass
        
    
    def addEvent(self, eventType, event):

        if(eventType in self.__envents):
            self.__envents[eventType].append(event)
        else:
            self.__envents[eventType] = [event]
        

    #end of addEvent

    def delEvent(self, eventType, event):
        
        if(eventType in self.__envents):
            try:
                self.__envents[eventType].remove(event)
                return True    
            except:
                return False
    
    #end of delEvent
    