#
# @lc app=leetcode.cn id=1329 lang=python3
# @lcpr version=30305
#
# [1329] 将矩阵按对角线排序
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        matrix = [[0] * n for _ in range(m)]
        dia_map = {}
        for j in range(n):
            key = (0, j)
            dia_map[key] = []
            i = 0
            tj = j
            while i < m and tj < n:
                dia_map[key].append(mat[i][tj])
                i += 1
                tj += 1
        
        for i in range(1, m):
            key = (i, 0)
            dia_map[key] = []
            ti = i
            j = 0
            while ti < m and j < n:
                dia_map[key].append(mat[ti][j])
                ti += 1
                j += 1
        
        for k, v in dia_map.items():
            v.sort()
            i, j = k
            t = 0
            while i < m and j < n:
                matrix[i][j] = v[t]
                i += 1
                j += 1
                t += 1
        
        return matrix
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[3,3,1,1],[2,2,1,2],[1,1,1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]\n
# @lcpr case=end

#

