import os


class IniParser(object):
    def __init__(self):
        self.data = dict()
    #end of init

    def read(self, f):
        section = self.data
        for line in f:
            line = line.strip()
            
            try:
                line = line [0:line.index("#")].strip()
            except:
                pass

            if(line.startswith("[") and line.endswith("]")):
                if(not(line[1:-1] in self.data)):
                    self.data[line[1:-1]] = dict()
                section = self.data[line[1:-1]]

            elif(line):
                name, value = line.split("=")
                section[name.strip()] = value.strip()
    
    def write(self, f):
        for sec in self.data:
            f.write("[%s]\n" % sec)
            for v in self.data[sec]:
                f.write("%s = %s\n" % (v, self.data[sec][v]))
            f.write("\n")


    def get(self, section, name):
        return self.data[section][name]

    def getboolean(self, section, name):
        val = self.get(section, name)
        return val.lower() in ["true", "1"]

    def getfloat(self, section, name):
        return float(self.get(section, name))

    def getint(self, section, name):
        return int(self.get(section, name))
    