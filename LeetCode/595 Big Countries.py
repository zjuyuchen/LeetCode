# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:05:32 2017

@author: yc
"""

# Write your MySQL query statement below
SELECT name, population, area 
FROM World 
WHERE  area > 3000000 OR population > 25000000