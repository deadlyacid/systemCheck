import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import datetime, time


class SystemCheck(object):
    ynetUrl = 'http://ynet.co.il'
    content = ''

    def __init(self):
        self.getContent()
        self.parseContent()

    def getContent(self):
        self.content = urllib2.urlopen(self.ynetUrl)
        return self.content

    def parseContent(self):
        soup = BeautifulSoup(self.content)
        result = soup.find("div", {"class" : "top-story-date"}).find("img")
        if result is not None:
            ynetDate = str(result["alt"]).split(" ")
            todatDate = datetime.now()
            todatDate = datetime.strftime(todatDate, "%d/%m/%Y")
            ynetDatetimeObj = datetime.strptime(ynetDate[0], '%d/%m/%Y')
            ynetDatetimeObj = ynetDatetimeObj.today().strftime('%d/%m/%Y')

            print ynetDatetimeObj == todatDate
        else:
            print 'Error not found!'
        pass


if __name__ == "__main__":
    myCheck = SystemCheck()
    myCheck.getContent()
    myCheck.parseContent()
