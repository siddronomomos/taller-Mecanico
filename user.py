
class user:
    def __init__(self):
        self.id = None
        self.name = None
        self.username = None
        self.password = None
        self.profile = None
    
    def setID(self, id):
        self.id = id
        return True
    
    def setName(self, name):
        self.name = name
        return True
    
    def setUsername(self, username):
        self.username = username
        return True
    
    def setPassword(self, password):
        self.password = password
        return True
    
    def setProfile(self, profile):
        self.profile = profile
        return True
    
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password
    
    def getProfile(self):
        return self.profile
