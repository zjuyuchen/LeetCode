# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:40:42 2017

@author: yc
"""

# Write your MySQL query statement below
SELECT FirstName, LastName, City, State FROM Person
LEFT JOIN Address
on Person.PersonId = Address.PersonID