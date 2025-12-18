#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30305
#
# [48] 旋转图像
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return
        # 先按照对角线旋转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 之后把每一行反转，结果就是旋转90度
        for i in range(n):
            p1 = 0
            p2 = n - 1
            while p1 <= p2:
                matrix[i][p1], matrix[i][p2] = matrix[i][p2], matrix[i][p1]
                p1 += 1
                p2 -= 1
                
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

