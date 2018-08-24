import os
from item_constructor import RomDataEntry


class Executor(object):
    def __init__(self,rules = dict()):        
        self.use_system = True
        self.rules = rules

    def exec(self, path, resolve = True):
        command = path
        if(resolve):
            command = self.resolve(command)
        
        print("%s Try exec: %s" % (self.__class__.__name__ , command))
        try:
            if self.use_system:
                return self.exec_system(command)
        except Exception as e:
            print("%s Error:%s" % (self.__class__.__name__ , e))
            return -1
    #end of exec

    def exec_system(self, command):
        return os.system('\"%s\"' % command)
    
    #end of exec_system

    def resolve(self, path):
        if(os.path.isdir(path)):
            return path

        ext = os.path.splitext(path)[1][1::].upper()

        if(ext in self.rules):
            return self.generate(self.rules[ext], path)

        #if cant select and there are rule for it 
        if("OTHER" in self.rules):
            return self.generate(self.rules["OTHER"], path)

        return path
    
    #end of resolve    

    def generate(self, rule, path):
        rule = rule.replace("%f", ('\"%s\"' % path)) # replace full file name with path
        
        name = os.path.splitext(os.path.basename(path))[0]
        rule = rule.replace("%name", name) # replace name without ext
        return rule
    #end of generate
    
#end of Executor

class RomExecutor(Executor):
    def __init__(self):
        Executor.__init__(self)
    
    def exec(self, romData, fullscreen = True):
        if(isinstance(romData, RomDataEntry)):
            command = romData.cmdwin
            if(fullscreen):
                command = romData.cmdfs
            
            command = command.replace("%f", ('\"%s\"' % romData.rom))
           
            Executor.exec(self,command, False)

        return -1
#end of ReomExecutor