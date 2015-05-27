# -*- coding: utf-8 -*-
import json
import urllib2
import urllib
import sys
import sqlite3
reload(sys)
sys.setdefaultencoding('gbk')

conn = sqlite3.connect('movie250.db')
print 'connect db'

url = 'https://api.douban.com/v2/movie/top250?start=200&count=100'
content = urllib2.urlopen(url)
content_read = content.read()
content_json = json.loads(content_read, 'utf-8')['subjects']
for i in content_json:
	conn.execute("insert into movie(name, rating, images, year)\
		values(?, ?, ?, ?)" , (i['title'], float(i['rating']['average']), str(i['images']['large']), int(i['year'])))
	#print 
conn.commit()
print 'success!'
#print len(content_json)
conn.close()
