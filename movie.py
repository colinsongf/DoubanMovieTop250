# -*- coding: utf-8 -*-
import os
import re
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')
import sqlite3
#处理种子

conn = sqlite3.connect('movie250.db')

def getFileList(p):
	p = str(p)
	if p == '':
		return []
	if p[-1] != '/':
		p = p + '/'
	a = os.listdir(p)
	b = [x for x in a if os.path.isfile(p+x)]
	return b

file = getFileList('Movie')
j = 0

for i in file:
#	matchObj = re.findall(r'(?:\S+)\W+\.', i)
	matchObj = re.findall(r'\S+\.', i)
	#print i
	if matchObj:
		movieName = matchObj[0][:-1]
		cursor = conn.execute('select id, name from movie where name like "%s"' % movieName )
		if cursor:
			#conn.execute('update movie set exist = 1 where name like "%s"' % movieName)
			for i in cursor:
				print i[0]
				os.rename('Movie/%s' % (movieName+'.torrent'), 'Movie/%s' % ('['+ str(i[0]) + ']' + movieName + '.torrent'))

			j += 1
			conn.commit()
		else:
			print movieName + 'error'
		#print 'success!'
	else:
		print 'not'

#print j
conn.close()