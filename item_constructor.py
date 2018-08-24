import os
import csv
from shlex import quote

class BaseItemConstructor(object):
    def __init__(self):
        self.all = []

    def next(self, id):
        return True


class DirlistItemConstructor(BaseItemConstructor):

    def __init__(self, startPath, executor = None):
        BaseItemConstructor.__init__(self)
        self.executor = executor
        self.set_path(startPath)
    # enf of init

    def collect(self):

        self.all = ["../"]

        try:
            _path_and_dir = list(os.listdir(self.currentPath))
            self.all += list(filter(lambda x: os.path.isdir(
                self.currentPath + '/' + x), _path_and_dir))
            self.all += list(filter(lambda x: os.path.isfile(
                self.currentPath + '/' + x), _path_and_dir))

        except Exception as e:
            print(e)

    def set_path(self, path):
        self.currentPath = path
        self.collect()

    def next(self, id):

        path = os.path.normpath(self.currentPath + "/" + self.all[id])
        if(os.path.isdir(path)):
            self.set_path(path)
            return True

        if(self.executor != None):
            return self.executor.exec(path)
        return False


class RomDataEntry(object):
    def __init__(self, data):
        
        self.rom, self.console, self.name, self.publ, self.cmdfs, self.cmdwin, self.cover, self.screens = data
        self.rom = self.rom.strip()
        self.console = self.console.strip().upper()
        self.publ = self.publ.strip()
        self.cmdfs = self.cmdfs.strip()
        self.cmdwin = self.cmdwin.strip()
        #self.screens = self.screens.split('|')
    
    # end of init

    def __repr__(self):
        return ', '.join([self.name, self.console, self.rom])
    
    def __str__(self):
        return self.name

class RomDataItemsConstructor(BaseItemConstructor):

    def __init__(self, manifestPath):

        BaseItemConstructor.__init__(self)
        self.manifestPath = manifestPath
        self.all = []
        self.partials = dict()

        self.parse()
    # end of init

    def getConsole(self, console):
        
        if(not (console in self.partials)):
            self.partials[console] = BaseItemConstructor()
        
        _partial = self.partials[console]
        _partial.all = [item for item in self.all if item.console.upper().strip() == console]
        
        return _partial
    #end of getConslole

    def parse(self):

        try:
            reader = csv.reader(open(self.manifestPath, 'r'))
            for row in reader:
                item = RomDataEntry(row)
                self.all.append(item)
        except Exception as e:
            print("CVS parsing error: ", e)

    # end of parse
