# -*- coding: utf-8 -*-
import os
from flask import render_template, redirect, url_for
from app import app
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')

import sqlite3

db = sqlite3.connect(app.config['DATABASE'], check_same_thread = False)


@app.route('/<int:no>')
def index(no):
	if no % 25 == 0:
		
		cur = db.execute('select id, name, images, rating, submary, doubanurl from movie order by id limit ?, 25', (no,))
		entries = [dict(id = cursor[0], name=cursor[1], images=cursor[2], rating=cursor[3], submary=cursor[4], doubanurl=cursor[5]) for cursor in cur.fetchall()]
		return render_template('index.html', entries=entries, no=no)
	else:
		return redirect('/ero')

@app.route('/')
def index2():
	return redirect('/0')

@app.route('/about')
def about():
	return render_template('/about.html')