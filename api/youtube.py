from pytube import YouTube

class Download:

    def __init__(self, url):
        self.url = url

    def downloadVideo(self):
        YouTube(self.url).streams.first().download()