# -*- coding:utf-8 -*-
#environment:python2.7
import string
import xml.dom.minidom
import re
import imp
class GetXml:
    """the class to get xml data"""

    def __init__(self):
        """initialize the class"""
        self.phish_list=[]

    def parse_xml(self,file_path):
        """
        Handle xml file with invalid character
        [input] : path of the xml file
        [output] : self.phish_list
        """
        try:
            xmldoc = xml.dom.minidom.parse(file_path)
        except:
            f = open(file_path)
            s = f.read()
            f.close()
            ss = s.translate(None, string.printable)
            s = s.translate(None, ss)
            try:
                phish_list=re.findall("<entry>.*?<url>(.*?)</url>.*?<phish_id>(.*?)</phish_id>.*?<phish_detail_url>(.*?)</phish_detail_url>.*?</entry>",s,re.S)
                for phish in phish_list:
                    self.phish_list.append(phish)
                #test the values of tuple
                """count=0
                for phish in phish_list:
                    print(phish)
                    count+=1
                print(count)"""
            #print("write successful!")
            except Exception as e:
                print e

#        xmldoc = xml.dom.minidom.parseString(s)
#    return xmldoc
 
 #test the class 
"""if __name__ == '__main__':
    getxml=GetXml()
    getxml.parse_xml("online-valid.xml")
    print getxml.phish_list"""
