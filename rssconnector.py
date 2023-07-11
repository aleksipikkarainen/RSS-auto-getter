import feedparser

class Rssparser:
    def __init__(self) -> None:
        self.shows = []
        pass

    def setRss(self):
        self.rss = input("Enter RSS address")

    def getRss(self):
        print(self.rss)

    def parseTest(self):
        d = feedparser.parse(self.rss)
        for x in d['entries']:
            print(x.title)
    
    def addShows(self):
        show = input("Please enter a show")
        if self.doesContain(show):
            print("Exists")
        else: 
            print("Doesn't exist")
    
    def doesContain(self, show):
        d = feedparser.parse(self.rss)
        for x in d['entries']:
            if x.title.__contains__(show):
                return True
        return False