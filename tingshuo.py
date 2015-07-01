#!/usr/bin/env python  
import tornado.ioloop
import tornado.web
import MySQLdb
import hashlib
import json
import sys
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

#DB_HOST = '''42.121.144.167'''
#DB_NAME = '''tingshuo'''
#DB_USER = '''shike'''
#DB_PASSWD = '''123456'''
 
config = ConfigParser.ConfigParser()
config.readfp(open(raw_input("input config file name:"), "rb"))
DB_HOST = config.get("global", "db_host")
DB_NAME = config.get("global", "db_name")
DB_USER = config.get("global", "db_user")
DB_PASSWD = config.get("global", "db_pass")

def testjson():
	result = {}
	result["name"] = "shike";
	result["nick"] = "xizhilang";
	result["age"]  = "32";
	print json.dumps(result);

def testnotic():
	notice = {}
	notice["notice"] = "this is test notice";
	print json.dumps(notice);

def get_user_id(acc):
	try:
		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
		cur = conn.cursor()
		sql = "select id, nickname from member where account=\'" + acc + "\'";
		result = cur.execute(sql);
		uid = 0;
		for id, nickname in cur.fetchall():
			print id, nickname, '\n';
			uid = id;
		conn.commit();
		cur.close();
		conn.close();
		return uid;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return "";

def get_user_acc(uid):
	try:
		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
		cur = conn.cursor()
		sql = "select account, nickname from member where id=" + uid;
		print sql, "\n";
		result = cur.execute(sql);
		acc = "";
		for account, nickname in cur.fetchall():
			acc = account;
		conn.commit();
		cur.close();
		conn.close();
		return acc;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return "";

def get_user_read_msg_id(acc):
	try:
		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
		cur = conn.cursor()
		sql = "select id, readmsgno from member where account=\'" + acc + "\'";
		result = cur.execute(sql);
		msgno = 0;
		for id, readmsgno in cur.fetchall():
			msgno = readmsgno;
		conn.commit();
		cur.close();
		conn.close();
		return msgno;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return "";

def add_like(msgid):
	try:
		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
		cur = conn.cursor()
		sql1 = "update message set likecnt = likecnt + 1 where id="+msgid;
		cur.execute(sql1);
		sql2 = "update member  set gold = gold + 2 , totallike = totallike +1 where id = (select uid from message where id=" +msgid + ")";
		cur.execute(sql2);
		conn.commit();
		cur.close();
		conn.close();
		return 1;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return "";

def add_gold(uid, num):
	try:
		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
		cur = conn.cursor()
		sql = "update member set gold = gold+"+num+" where id="+uid;
		conn.commit();
		cur.close();
		conn.close();
		return 1;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return "";

def del_gold(uid, num):
	try:
		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
		cur = conn.cursor()
		sql = "update member set gold = gold-"+num+" where id="+uid;
		conn.commit();
		cur.close();
		conn.close();
		return 1;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return "";

def get_user_info(acc):
	try:
		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
		cur = conn.cursor()
		sql = "select nickname, avatar, gold, ''like'' from member where account=\"" + acc + "\"";
		print sql, acc;
		print "\n";
		result = cur.execute(sql);

		nik = "";
		avt = "";
		gld = 0;
		lik = 0;
		for nickname , avatar, gold , like in cur.fetchall():
			print nickname, avatar, gold, like;
			nik = nickname;
			avt = avatar;
			gld = gold;
			lik = like;
		conn.commit();
		cur.close();
		conn.close();
	
		info = {};
		info["acc"] = acc;
		info["nik"] = nik;
		info["avt"] = avt;
		info["gold"] = gld;
		info["lik"] = lik;
		all = {};
		all["info"] = info;
		return json.dumps(all);
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return "";
	

def valid_user(acc, passwd):
	try:
       		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
        	cur=conn.cursor()
		sql = "select account from member where account=\'"+acc+"\' and password=\'"+passwd+"\'";
		print sql; print '\n';
		result = cur.execute(sql);
		conn.commit();
		cur.close();
		conn.close();
		if result == 1:
			print "--valid user ", acc;
			return 1;
		else:
			print "--invalid user ", acc;
			return 0;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return 0;

def getmd5(str):
	return hashlib.md5(src).hexdigest().upper();

def procLogon(acc, passwd):
	print acc, "is logon...";
	try:
       		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
        	cur=conn.cursor()
		sql = "select * from member where account=\'"+acc+"\' and password=\'"+passwd+"\'";
		print sql; print '\n';
		result = cur.execute(sql);
		conn.commit();
		cur.close();
		conn.close();
		if result == 1:
			return 1;
		else:
			return 0;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return 0;
	
		
def procRegist(acc, passwd):
        print acc, "is regist...";
	try:
       		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
        	cur=conn.cursor()
        	value = [acc, passwd]
		print value,'\n';
		result = cur.execute('insert into member(account, password) values(%s,%s)',value)
		conn.commit();
		cur.close();
		conn.close();
		return 1;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return 0;

def procModify(acc, passwd, item, value):
	print acc, "is modify ",item , "to ", value; 
	if 0 == valid_user(acc, passwd):
		return 0;
	try:
       		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
        	cur=conn.cursor()
		field = "nickname"
		if item=="psw":
			field = "password"
		elif item=="nk":
			field = "nickname"
		elif item=="g":
			field = "gender"
			if value!="m" and value!="f":
				return 0;
		elif item=="avt":
			field = "avatar"
		else:
			print "unkown modify item name"
			return 0;
			
		#value = [field, value, acc, passwd]
		sql = "update member set " + field + "=\'" + value +  "\' " + "where account=\'" + acc + "\' and password=\'" + passwd + "\'";
		print sql;
		result = cur.execute(sql);
		#result = cur.execute("update member set %s = %s where account=%s and password=%s", value);
		print result;
		conn.commit();
		cur.close();
		conn.close();
		return 1;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return 0;

def save_msg(acc, msg):
	print "save user(", acc, ") msg :" , msg , '\n';
	try:
       		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
        	cur=conn.cursor()
		uid = get_user_id(acc);
        	value = [uid, msg]
		result = cur.execute('insert into message(uid, msg) values(%s,%s)', value)
		conn.commit();
		cur.close();
		conn.close();
		return 1;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return 0;
	
def get_unread_msg(acc, msgs, curpage, pagesize):
	try:
		#print "cur %s pagesize %s" % (curpage, pagesize)
       		conn = getDBConn('''tingshuo''')
		conn.select_db('tingshuo')
        	cur=conn.cursor()
		readmsgno = get_user_read_msg_id(acc);
		sqlstr = "select id,unix_timestamp(createtime) as time, likecnt, uid, msg from message where id>%s and createtime>DATE_SUB(now(), INTERVAL 1 DAY) order by id DESC limit %s,%s" % (readmsgno, curpage, pagesize)
		print sqlstr
		result = cur.execute(sqlstr);
		for id, time, likecnt, uid, msg in cur.fetchall():
			one = {};
			one["id"]	= id;
			one["msg"]	= msg;
			one["t"]	= time;
			one["uid"]	= uid;
			one["like"]	= likecnt;
			jsonstr = json.dumps(one);
			msgs.append(jsonstr);
		print msgs;
		conn.commit();
		cur.close();
		conn.close();
		return 1;
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		return 0;
	
		info = {};
		info["acc"] = acc;
		info["nik"] = nik;
		info["avt"] = avt;
		info["gold"] = gld;
		all = {};
def getDBConn(dbname):
        conn=MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, port=3306,charset="utf8")
        return conn

class MainHandler(tornado.web.RequestHandler):
        def get(self):
		#testjson();
                t = self.get_argument('type');
                if t=="reg":
                	print "start reg..."
                	acc = self.get_argument('acc')
                	pas = self.get_argument('psw')
			r = procRegist(acc, pas);
			if r == 1:
                		self.write("regist ok.")
			elif r == 0:
                		self.write("regist failed. account is used.")
			else:
                		self.write("regist failed.")
                elif t=="logon":
                	print "start logon..."

                	acc = self.get_argument('acc')
                	pas = self.get_argument('psw')
                        r = procLogon(acc, pas)
			if r == 1:
                		self.write("logon ok.")
			else:
                		self.write("logon failed.")
		elif t=="modify":
			print "start modify..."
                	acc = self.get_argument('acc')
                	pas = self.get_argument('psw')
			item= self.get_argument('item')
			value=self.get_argument('value')
                        r = procModify(acc, pas, item, value)
			if r == 1:
                		self.write("modify ok.")
			else:
                		self.write("modify failed.")

		elif t=="getinfo":
			print "get user info..."
                	acc = self.get_argument('acc')
                	pas = self.get_argument('psw')
			#get user info
			if 1 == valid_user(acc, pas):
				info = get_user_info(acc);
				self.write(info);
	
		elif t=="hb":
			print "hart beat..."
                	acc = self.get_argument('acc')
                	pas = self.get_argument('psw')
			cup = self.get_argument('curpage')
			pgs = self.get_argument('pagesize')
			r = valid_user(acc, pas)
			if r == 1:
				msgs = [];
				get_unread_msg(acc, msgs, cup, pgs);
				for msg in msgs:
					#print msg;
					self.write(msg);
			else:
				self.write('hb err');
		elif t=="msg":
			print ""
			acc = self.get_argument('acc');
                	pas = self.get_argument('psw')
			r = valid_user(acc, pas)
			if r == 1:
				msg = self.get_argument('msg');
				sr = save_msg(acc, msg.encode('utf8'));
				if sr==1:
					self.write("pub msg ok");
				else:
					self.write("pub msg failed");
			else:
				self.write('recv msg err');
		elif t=="query_u_info":
			#acc = self.get_argument('acc');
                	#pas = self.get_argument('psw')
			uid = self.get_argument('uid');
			#r = valid_user(acc, pas)
			r = 1;
			if r == 1:
				acc = get_user_acc(uid);
				info = get_user_info(acc);
				#print jsonstr;
				self.write(info);
			else:
				self.write('invalid user');
		elif t=="like":
			acc = self.get_argument('acc');
                	pas = self.get_argument('psw')
			msgid = self.get_argument('msgid');
			r = valid_user(acc, pas)
			if r == 1:
				sr = add_like(msgid);
				if sr==1:
					self.write("add like ok");
				else:
					self.write("add like failed");
			else:
				self.write('recv msg err');
		elif t=="addgold":
			acc = self.get_argument('acc');
                	pas = self.get_argument('psw')
			r = valid_user(acc, pas)
			if r == 1:
				sr = add_gold(acc);
				if sr==1:
					self.write("add gold ok");
				else:
					self.write("add gold failed");
			else:
				self.write('recv msg err');
		elif t=="delgold":
			acc = self.get_argument('acc');
                	pas = self.get_argument('psw')
			num = self.get_argument('num');
			r = valid_user(acc, pas)
			if r == 1:
				uid = get_user_id(acc);
				sr = del_gold(acc);
				if sr==1:
					self.write("del gold ok");
				else:
					self.write("del gold failed");
			else:
				self.write('recv msg err');
                else:
                	self.write("invalid op type")



application = tornado.web.Application([ 
    (r"/", MainHandler),
])  

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start();

