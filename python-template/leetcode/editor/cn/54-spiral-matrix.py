#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30305
#
# [54] 螺旋矩阵
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        nums = []
        p1 = 0 # 左界
        p2 = n - 1 # 右界
        p3 = 0 # 上界
        p4 = m - 1 # 下界
        
        while p1 <= p2 or p3 <= p4:
            if p4 >= p3:
                # 右
                for i in range(p1, p2 + 1):
                    nums.append(matrix[p3][i])
                p3 += 1
            
            if p2 >= p1:
                # 下
                for i in range(p3, p4 + 1):
                    nums.append(matrix[i][p2])
                p2 -= 1
            
            if p4 >= p3:
                # 左
                for i in range(p2, p1 - 1, -1):
                    nums.append(matrix[p4][i])
                p4 -= 1
            
            if p2 >= p1:
                # 上
                for i in range(p4, p3 - 1, -1):
                    nums.append(matrix[i][p1])
                p1 += 1
            
        return nums
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = solution.spiralOrder(matrix)
    
    print(res)





#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

