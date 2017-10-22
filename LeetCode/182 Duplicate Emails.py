# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 23:54:51 2017

@author: yc
"""
SELECT Email from Person
Group By Email
Having Count(*) > 1;