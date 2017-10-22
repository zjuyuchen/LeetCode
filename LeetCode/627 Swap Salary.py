# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:05:49 2017

@author: yc
"""

# Write your MySQL query statement below
UPDATE salary SET sex = IF(sex = 'm', 'f', 'm')