#-*-encoding=utf-8-*-
from prettytable import PrettyTable as pt
import sys
import requests 
import re	
import threading

# The main process of community.py
def com(): 
	global x,task
	task=[]

	x = pt(["Name","Area","Green Coverage"]) 
	x.padding_width = 1
	print '\033[2J\033[HData on monitoring. Requesting data from Internet...'
	for j in range(1,318):	
		task.append(1)
		thread = threading.Thread(target=loop,args=(j,))
		thread.start()
	loop_switch = 1
	total = 0
	while loop_switch:
		for i in task:
			total += i
		if total==0:
			loop_switch = 0
		total = 0
	print x
	print 'All requests successfully recorded.'
	pass

def loop(j):
	print '>>Thread %s has started.'%str(j)
	r = requests.get(url = 'http://hangzhou.fangtoo.com/building/cp' + str(j))
	name = re.findall(r'<a href=["]http://hangzhou.fangtoo.com/building/(.*)/["] target=["]_blank["] title=["](.*)["] target=["]_blank["]>',r.text)

	for i in range(1,len(name)):
		detail = requests.get(url = 'http://hangzhou.fangtoo.com/building/' + str(name[i-1][0]))
		area = re.findall(ur'<li>占地面积：(\d.*)平方米</li>',detail.text) 
		ve = re.findall(ur'<li>绿化率：(.*)</li>',detail.text)
		if area == []:
			area = [('--')]
	
		NAME = str(name[i-1][1].encode('utf-8'))
		AREA = str(area[0].encode('utf-8'))
		GREEN_COVERAGE = str(ve[0].encode('utf-8'))

		table_data = ([NAME,AREA,GREEN_COVERAGE])
		
		print NAME,AREA,GREEN_COVERAGE
		x.add_row(table_data)
	task.remove(1)
	print '>> Thread %s has finished.'%str(j)
	pass

def main(args):	
	com()
	
if __name__ == '__main__':
    sys.exit(main(sys.argv))
