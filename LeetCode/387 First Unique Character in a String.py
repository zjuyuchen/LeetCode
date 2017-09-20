class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
#        dic = {}
#        st = ''
#        for i in s:
#            if i not in dic:
#                dic[i] = 1
#            else:
#                dic[i] += 1
#        if not dic or min(dic.values()) >1:
#            return -1
#        for j in dic:
#            if dic[j] == 1:
#                st = j
#                break
#        for k in range(len(s)):
#            if st == s[k]:
#                return k
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                

        for k in range(len(s)):
            if dic[s[k]] == 1:
                return k
        return -1
test =Solution()
print(test.firstUniqChar('eetcode'))