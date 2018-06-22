import urllib.request
import re
import unicodedata


class Downloader:
    
    def __init__(self, url):
        self.url = url

    def downloadFile(self, file):
        pass  # TODO

    def getAsString(self):
        try:
            socket = urllib.request.urlopen(self.url)
            data = socket.read()
            socket.close()

            return data.decode("utf8")
        except Exception as exception:
            return str(exception)
