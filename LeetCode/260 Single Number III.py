# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:47:05 2017

@author: Demo
"""
#这个想法比较绕，xor = 0,对nums中所有num求异或，那么重复出现的所有数字两次异或以后对xor贡献1的个数就为0
#最终剩下来的两个以上的1就是两个不同的数字贡献的，比如 3 xor 5 = 0110
#下面是比较绕的地方。0110里面的两个1,肯定分别来源于两个数字。所以nums中3,5分别包含0010和0100.
#剩下的就是对所有倒数第二的位置为1（0010）的数字求异或，得到其中一个。在对剩下的数字求异或，得到剩下的一个。
#这个问题，面试十分钟能自己想出来，那得多聪明？？？


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        res = [0,0]
        for n in nums:
            xor ^= n
        mask = 1
        while(xor&mask == 0):
            mask = mask << 1
        for n in nums:
            if n&mask:
                res[0] ^= n
            else:
                res[1] ^= n
        return res
        