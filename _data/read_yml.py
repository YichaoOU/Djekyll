from yaml import load, dump
import sys
file = sys.argv[1]

with open(file, 'r') as stream:

	my_cat = load(stream)

#
for key in my_cat.keys():
	print key,my_cat[key][0]
'''
liyc@liyc-OU:/home/web/django/mysite/_data$ python read_yml.py catelog.yml 
tab2 ['qwe1', 'qwe2', 'qwe3']
tab1 ['abc1', 'abc2']
liyc@liyc-OU:/home/web/django/mysite/_data$ python read_yml.py catelog.yml 
tab2 qwe1
tab1 abc1
liyc@liyc-OU:/home/web/django/mysite/_data$ 

'''