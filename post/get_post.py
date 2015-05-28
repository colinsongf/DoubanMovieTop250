# -*- coding: utf-8 -*-
import os
import sqlite3
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')

import re

conn = sqlite3.connect('movie250.db')

post = conn.execute('select images, id from movie order by id')
j = 0
for i in post:
	url = i[0]
	url_id = i[1]
	matchObj = re.findall(r'p\d+.jpg', url)
	if matchObj:
		print url
		conn.execute('update movie set images = ? where id=?', (matchObj[0], url_id))
		conn.commit()
	j += 1
print j
conn.close()
