class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def smooth(c,i,j):
            count = 0       
            sums = 0
            a = [-1, 0, 1]
            for m in a:
                for n in a:
                    if i+m >=0 and i+m <len(c) and j+n >=0 and j+n < len(c[0]):
                        sums += c[i+m][j+n]
                        count += 1
            return sums//count
        result = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        for i, row in enumerate(M):
            for j, m in enumerate(row):
                result[i][j] = smooth(M, i, j)
        return result