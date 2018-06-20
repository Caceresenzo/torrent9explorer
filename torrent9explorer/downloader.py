import urllib.request
import re


class Downloader:

    def __init__(self, url):
        self.url = url

    def downloadFile(self, file):
        pass  # TODO

    def getAsString(self):
        socket = urllib.request.urlopen(self.url)
        data = socket.read()
        socket.close()

        return data.decode("utf8")
