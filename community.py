#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  community.py
#  
#  Copyright 2017-2019 Hisen Zhang <hisenzhang01@foxmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from __future__ import division
import requests 
import re	
import json
from prettytable import PrettyTable as pt
import statistic

def com():
	f = open('data.json','w+')
	t = open('datatable.txt','w+')
	x = pt(["NO.","Code","Name","Area","Green Coverage"]) 
	print '\033[2J\033[HData on monitoring. Requesting data from Internet...'
	
	for j in range(1,318):
		print '\n',j,'/ 317\n'
		r = requests.get(url = 'http://hangzhou.fangtoo.com/building/cp'+str(j))
		name = re.findall(r'<a href=["]http://hangzhou.fangtoo.com/building/(.*)/["] target=["]_blank["] title=["](.*)["] target=["]_blank["]>',r.text)
		x.padding_width = 1
		
		for i in range(1,len(name)):	
			detail = requests.get(url = 'http://hangzhou.fangtoo.com/building/'+str(name[i-1][0]))
			area = re.findall(ur'<li>占地面积：(\d.*)平方米</li>',detail.text) 
			ve = re.findall(ur'<li>绿化率：(.*)</li>',detail.text)
			
			if area == []:
				area = [('--')]
			
			json_data = json.dumps({'NO.':str(i+(j-1)*26).zfill(4),'ID':str(name[i-1][0].encode('utf-8')),'NAME':str(name[i-1][1].encode('utf-8')),'AREA':str(area[0].encode('utf-8')),'GREEN_COVERAGE':str(ve[0].encode('utf-8'))})
			show_data = ([str(i+(j-1)*26).zfill(4),str(name[i-1][0].encode('utf-8')),str(name[i-1][1].encode('utf-8')),str(area[0].encode('utf-8')),str(ve[0].encode('utf-8'))])
			print show_data
			x.add_row(show_data)
			f.writelines(json_data) 
										 	
	print x
	t.writelines(str(x)) 
	f.close
	t.close
	print 'All requests successfully recorded.'


def main(args):
    com()
    statistic.sta()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
