import configparser

class test:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read("rorole.conf")
        self.roles = self.conf.items("roles")
        for self.role in self.roles:
            self.swap = self.role[0]
            self.role[0] = self.role[1]
            self.role[1] = self.swap
        print(self.roles)


test()