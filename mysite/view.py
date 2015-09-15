from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response as rtr
import settings
import os
from django.core.files import File
from django.template import Context
import re

import codecs
from yaml import load, dump
import markdown as md

# global vars
default_page = 'about-about-me.md'
with open('/home/web/django/mysite/_data/font_color.yml', 'r') as stream:
	font_color = load(stream)



def read_yaml():
	file = '/home/web/django/mysite/_data/catelog.yml'
	with open(file, 'r') as stream:
		my_cat = load(stream)
	return my_cat
#
# for key in my_cat.keys():
	# print key,my_cat[key][0]

def generate_tabs(my_cat,current):
	first_part = '\n<div id="pages" class="tabs">\n  <li class="Classic"><a class="menu-item " href="'
	thrid_part = '" target="_self">'
	fifth_part = '</a>'
	end_part = '</li>\n</div>\n'
	isCurrent = ' &#x25BC;'
	output = ""
	dict={}
	for key in my_cat.keys():
		dict[key] = 'http://127.0.0.1:8080/'+key+'/'+my_cat[key][0].replace(' ','-')+'.md'
	for key in dict.keys():
		if key == current:
			output += first_part + dict[key] + thrid_part + key + fifth_part + isCurrent + end_part
		else:
			output += first_part + dict[key] + thrid_part + key + fifth_part + end_part
	return output

def generate_sidebar(my_cat,current_tab,current_article):
	first_part = '\n<div class="item hentry '
	thrid_part = '">\n<h3 class="title entry-title">\n<a href="'
	img_part1 = '<img class="thumbnail" src="'
	img_part2 = '" style="width: 30px; height: 30px;">'
	fifth_part = '">'
	# href = ''
	# name = ''
	end_part = '</a>\n  </h3>\n</div>\n'
	output = ''
	for article in my_cat[current_tab]:
		href = 'http://127.0.0.1:8080/'+current_tab+'/'+article.replace(' ','-')+'.md'
		if current_article == (article.replace(' ','-')+'.md'):
			output += first_part + 'selected' + thrid_part + href + fifth_part + article + end_part
		else:
			output += first_part + thrid_part + href + fifth_part + article + end_part
	return output
def markdown_html(file):
	input_file = codecs.open(file, mode="r", encoding="utf-8")
	text = input_file.read()
	# preprocess for font color
	text = reduce(lambda x, y: x.replace(y, font_color[y]), font_color, text)
	html = md.markdown(text)
	return html
	
def generate_post(request,query):
	my_catelog = read_yaml()
	
	# filter empty strings
	catelog_array = filter(None, query.split('/'))
	# catelog_array is either 2 or 0
	''' may need to validate catelog_array in later version '''
	case = len(catelog_array)
	current_dir = os.path.dirname(os.path.abspath(__file__))
	post_dir = current_dir + '/../_posts/'
	post = ''
	if case == 0:
		post_md = post_dir + default_page
		post = markdown_html(post_md)
		header_tabs = generate_tabs(my_catelog,'about')
		sidebar = generate_sidebar(my_catelog,'about','about-me.md')
	if case == 2:
		post_md = post_dir + catelog_array[0] + '-' + catelog_array[1]
		post = markdown_html(post_md)
		header_tabs = generate_tabs(my_catelog,catelog_array[0])
		sidebar = generate_sidebar(my_catelog,catelog_array[0],catelog_array[1])
	# return HttpResponse(post)
	return rtr('main.html',{'title':'asd','post':post,'header_tabs':header_tabs,'sidebar_menu':sidebar})
	




