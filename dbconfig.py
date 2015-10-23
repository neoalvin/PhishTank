import MySQLdb
from config import MYSQL_HOST,MYSQL_USER,MYSQL_PWD
class DBConfig:
	def __init__(self):
		self.db=""
		self.count=1
	def create_db(self):
		"""create the db to sava data"""
		try:
			conn=MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PWD)
			cur=conn.cursor()
			cur.execute("create database if not exists phish")
			conn.close()
			print "create database successful!"
		except Exception as e:
			print e
		try:
			conn=MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PWD,db="phish")
			cur=conn.cursor()
			cur.execute("create table if not exists phish_list(phishid int primary key,phishurl text,phishdetail text)")	
			cur.close()
			conn.close()
			print "create table successful!"
		except Exception as e:
			print e

	def connect_db(self):
		"""connect the db"""
		try:
			self.db=MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PWD,db="phish")
			print "connect the db successful!"
		except Exception as e:
			print e

	def insert_db(self,values):
		"""insert data into db"""
		try:
			#self.connect_db()
			cur=self.db.cursor()
			cur.execute("insert into phish_list(phishurl,phishid,phishdetail) values(%s,%s,%s)",values)
			print "insert data into database successful!\nthe number of updated records:\t%d"%self.count
			self.db.commit()
			cur.close()
		except Exception as e:
			self.count-=1		#record the  number of insert values

	def select_db(self):
		"""select data from database"""
		try:
			#self.connect_db()
			cur=self.db.cursor()
			cur.execute("select * from phish_list")
			values=cur.fetchall()
			#print "select the data from database successful!"
			self.db.commit()
			cur.close()
			return values
		except Exception as e:
			print e

	def deldata_db(self):
		"""select data from database"""
		try:
			#self.connect_db()
			cur=self.db.cursor()
			cur.execute("delete from phish_list")
			print "delete data from table successful!"
			self.db.commit()
			cur.close()
		except Exception as e:
			print e

	def close_db(self):
		"""close the db"""
		self.db.close()
		print "the database has already closed!"

#test the class
"""if __name__=="__main__":
	myconfig=DBConfig()
	myconfig.connect_db()"""