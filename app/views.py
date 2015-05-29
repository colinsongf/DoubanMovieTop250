# -*- coding: utf-8 -*-
import os
from flask import render_template, redirect, url_for, request, flash
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from app import app
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')
import sqlite3

db = sqlite3.connect(app.config['DATABASE'], check_same_thread = False)


class SearchForm(Form):
	searchNo = StringField('searchNo', validators=[DataRequired()])

@app.route('/<int:no>', methods=['GET', 'POST'])
def index(no):
	form = SearchForm()
	if no % 25 == 0:
		cur = db.execute('select id, name, images, rating, submary, doubanurl from movie order by id limit ?, 25', (no,))
		entries = [dict(id = cursor[0], name=cursor[1], images=cursor[2], rating=cursor[3], submary=cursor[4], doubanurl=cursor[5]) for cursor in cur.fetchall()]
		if form.validate_on_submit():
			searchNo0 = form.searchNo.data
			result = db.execute('select id from movie where name like ?', ('%' + searchNo0 + '%',))
			for i in result:
				searchNo = i[0]

				if int(searchNo) <= 25:
					return redirect('/0#%d' % int(searchNo))
				if int(searchNo) <= 50:
					return redirect('/25#%d' % int(searchNo))
				if int(searchNo) <= 75:
					return redirect('/50#%d' % int(searchNo))
				if int(searchNo) <=100:
					return redirect('/75#%d' % int(searchNo))
				if int(searchNo) <=125:
					return redirect('/100#%d' % int(searchNo))
				if int(searchNo) <=150:
					return redirect('/125#%d' % int(searchNo))
				if int(searchNo) <=175:
					return redirect('/150#%d' % int(searchNo))
				if int(searchNo) <=200:
					return redirect('/175#%d' % int(searchNo))
				if int(searchNo) <=225:
					return redirect('/200#%d' % int(searchNo))
				if int(searchNo) <=250:
					return redirect('/225#%d' % int(searchNo))
				else:
					return redirect('/404')
			if result.fetchall()  == []:
				return redirect('/404')
	else:
		return redirect('/ero')
	return render_template('index.html', entries=entries, no=no, form=form)

@app.route('/')
def index2():
	return redirect('/0')

@app.route('/about')
def about():
	return render_template('/about.html')

