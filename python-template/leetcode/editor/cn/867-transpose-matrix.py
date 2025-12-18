#
# @lc app=leetcode.cn id=867 lang=python3
# @lcpr version=30305
#
# [867] 转置矩阵
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        matrixT = [[0] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                matrixT[j][i] = matrix[i][j]
        
        return matrixT
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#

