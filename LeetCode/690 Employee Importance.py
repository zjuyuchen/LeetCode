# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:36:43 2017

@author: Administrator
"""

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        for e in employees:
            if e.id == id:
                temp = e
                break
        return temp.importance + sum([self.getImportance(employees, i) for i in temp.subordinates])