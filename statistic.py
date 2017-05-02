#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sta.py
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
import re
import sys
from prettytable import PrettyTable as pt


def sta():
	with open('data.json','r+') as f:
			x = f.readlines()
	l = re.findall(r'["]([0-9]*[\.]*[0-9]+)%["]',str(x))
	print len(l),'data is valid for statistic.\n'
	counter_0 = 0
	counter_1 = 0
	counter_2 = 0
	counter_3 = 0
	counter_4 = 0
	
	for i in range(0,len(l)):
		if float(l[i])<10:
			counter_0 = counter_0 + 1
		if float(l[i])>=10 and float(l[i])<25:
			counter_1 = counter_1 + 1
		if float(l[i])>=25 and float(l[i])<40:
			counter_2 = counter_2 + 1
		if float(l[i])>=40 and float(l[i])<55:
			counter_3 = counter_3 + 1
		if float(l[i])>55:
			counter_4 = counter_4 + 1
			
	tb = pt(["COVERAGE RANGE","COUNT","PERCENTAGE",]) 	
	tb.align["COUNT"] = "r" 
	tb.add_row(["x<10",counter_0,float(counter_0/len(l)*100)])
	tb.add_row(["10<=x<25",counter_1,float(counter_1/len(l)*100)])
	tb.add_row(["25<=x<40",counter_2,float(counter_2/len(l)*100)])
	tb.add_row(["40<=x<55",counter_3,float(counter_3/len(l)*100)])	
	tb.add_row(["x>55",counter_4,float(counter_4/len(l)*100)])
	print tb
	
