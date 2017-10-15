# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:06:15 2017

@author: yc
"""

# Write your MySQL query statement below
SELECT (CASE 
    WHEN mod(id, 2) != 0 and records != id THEN id + 1
    WHEN mod(id, 2) != 0 and records = id THEN id
    ELSE id - 1
END) AS id, student
FROM seat, (SELECT COUNT(*) AS records FROM seat) as seat_records
ORDER BY id ASC
