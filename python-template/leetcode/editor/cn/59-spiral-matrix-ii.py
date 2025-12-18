#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30305
#
# [59] 螺旋矩阵 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            matrix.append([0]*n)
        
        i = 1
        nums = n * n
        p1 = 0 # 上
        p2 = n - 1 # 下
        p3 = 0 # 左
        p4 = n - 1 # 右
        while i <= nums:
            if p2 >= p1:
                for j in range(p3, p4 + 1):
                    matrix[p1][j] = i
                    i += 1
                p1 += 1
            
            if p4 >= p3:
                for j in range(p1, p2 + 1):
                    matrix[j][p4] = i
                    i += 1
                p4 -= 1
            
            if p2 >= p1:
                for j in range(p4, p3-1, -1):
                    matrix[p2][j] = i
                    i += 1
                p2 -= 1
            
            if p4 >= p3:
                for j in range(p2, p1-1, -1):
                    matrix[j][p3] = i
                    i += 1
                p3 += 1
        
        return matrix
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

