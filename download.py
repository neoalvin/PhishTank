#coding:utf-8
import urllib
import urllib2
import datetime
from time import sleep

class DownloadXml:
    """the program to get phish sites"""

    def __init__(self):
        """initialize the class"""
        self.key="d743564c35a46d3fb979e480397f0bdbc9249028e88eb19139781cac40d9946d"
        self.filename="online-valid.xml"
        self.url="http://data.phishtank.com/data/"+self.key+"/"+self.filename
        self.retrytime=5        #the times what the downloading can retry
        self.sleeptime=3        #the sleep time between twice attempts

    def download(self):
        """download the package"""
        start=datetime.datetime.now()
        f=urllib2.urlopen(self.url)
        print "The downloading start.\nstart time:%s"%start
        print "URL:"+self.url
        data=f.read()
        with open(self.filename, "wb") as code:
            code.write(data)
        end=datetime.datetime.now()
        print "The package downloaded.\nfinish time:%s"%end
        costtime=end-start
        coststr=costtime.second+' seconds'
        print "cost time:%s"%coststr

    def retrydownload(self):
        """retry the downloading if error"""
        retrycount=0
        while True:
            try:
                self.download()
                break
            except Exception as e:
                if retrycount<self.retrytime:
                    retrycount+=1
                    print e
                    print "The downloading will retry after "+str(self.sleeptime)+" seconds."
                    sleep(self.sleeptime)
                    continue
                else:
                    msg="It retrys "+str(retrycount)+" times.But it doesn't work successful! Please check it."
                    raise Exception(msg)

#test the class 
if __name__=="__main__":
    downloadxml=DownloadXml()
    downloadxml.retrydownload()
    
