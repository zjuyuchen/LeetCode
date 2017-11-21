# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:35:20 2017

@author: Demo
"""

class Codec:
    def __init__(self):
        self.dic = {}
        self.count = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.dic:
            self.dic[longUrl] = self.count
            self.count += 1
        return "http://tinyurl.com/"+str(self.dic[longUrl])
        
        
    def findKey(self,dic,val):
        for d in dic:
            if dic[d] == val:
                return d
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        s = int(shortUrl[19:])
        shortUrl = self.findKey(self.dic, s)
        return shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))