# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:14:40 2017

@author: yc
"""
time = 1
def a(x,time=time+1):
    if time<3:
        print(x)
        time +=1
        a(x)
        print('middle')
        print(time)
a('x')
        