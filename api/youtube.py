from pytube import YouTube

class Download:

    def __init__(self, url):
        self.url = url

    def downloadVideo(self):
        yt = YouTube(self.url).streams.first().download()
        print(yt.title)

#debuing is valid
if __name__ == "__main__":
    dow = Download("URL")
    dow.downloadVideo()