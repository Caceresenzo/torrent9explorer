#

class Torrent9Item():
    
    INCREMENT = 0

    def __init__(self, type, url, name, size, seed, leech):
        self.id = Torrent9Item.incrementId()
        self.type = type
        self.url = url
        self.name = name.replace("<span style=\"color:#337ab7\">", "").replace("</span>", "") # Search add "blue text" to match search query 
        self.size = size
        self.seed = seed
        self.leech = leech

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getUrl(self):
        return self.type

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getSeed(self):
        return self.seed

    def getLeech(self):
        return self.leech
    
    @staticmethod
    def incrementId():
        Torrent9Item.INCREMENT = Torrent9Item.INCREMENT + 1
        return Torrent9Item.INCREMENT