#coding:utf-8
from dbconfig import DBConfig
from getphish import GetXml
from download import DownloadXml
import time

def test_db():
	"""test the db operation."""
	myconfig=DBConfig()
	myconfig.connect_db()
	values=['www.aaa.com','555','www.bbb.com']
	myconfig.insert_db(values)
	print myconfig.select_db()
	myconfig.deldata_db()
	myconfig.close_db()

def test_createdb():
	"""create database"""
	myconfig=DBConfig()
	myconfig.create_db()

def test_download():
	"""test the downloading of xml file"""
	downloadxml=DownloadXml()
	filename=downloadxml.filename
	#download the xml file to lcoal file
	downloadxml.retrydownload()

def test_xmlread():
	"""test the process of xml reading"""
	getxml=GetXml()
	downloadxml=DownloadXml()
	#get the name of xml file
	filename=downloadxml.filename
	#get the list from xml file
	getxml.parse_xml(filename)
	phish_list=getxml.phish_list
	return phish_list

def xml_to_db():
	"""insert into database from xml file"""
	myconfig=DBConfig()
	phish_list=test_xmlread()
	myconfig.connect_db()
	try:
		for phish in phish_list:
			myconfig.insert_db(phish)
			myconfig.count+=1
		myconfig.close_db()
		print "The phish list have already inserted into database"
	except Exception as e:
		print e

def do_action_main():
	"""the main func to execute the program"""
	#get the object for the class
	test_download()
	xml_to_db()

def do_action():
	xml_to_db()

def timer():
	"""set a timer to execute this program"""
	while True:
		print "the program start at "+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
		do_action_main()
		time.sleep(10800)

if __name__=="__main__":
	print('1-create the database we need\n2-execute without downloading and updating on time\n3-execute main program')
	choice=int(input("choose the number:"))
	if choice==1:
		test_createdb()
	elif choice==2:
		do_action()
	elif choice==3:
		timer()
	else:
		print "Input error,Please check it and restart the program"

	
