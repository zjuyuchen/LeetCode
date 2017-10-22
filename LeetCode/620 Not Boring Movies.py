# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:03:49 2017

@author: yc
"""

# Write your MySQL query statement below
SELECT *
FROM cinema
WHERE id % 2 = 1 AND NOT description = 'boring'
ORDER BY rating DESC