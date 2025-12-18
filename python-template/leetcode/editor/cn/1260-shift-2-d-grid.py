#
# @lc app=leetcode.cn id=1260 lang=python3
# @lcpr version=30305
#
# [1260] 二维网格迁移
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        num =  m * n
        k = k % num
        new_grid = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = (i * n + j) + k
                new_i = (idx // n) % m
                new_j = idx % n
                new_grid[new_i][new_j] = grid[i][j]
        
        return new_grid
            
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    res = solution.shiftGrid(grid, k)
    print(res)





#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n9\n
# @lcpr case=end

#

