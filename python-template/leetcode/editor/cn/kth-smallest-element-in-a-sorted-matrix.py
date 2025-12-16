#
# @lc app=leetcode.cn id=378 lang=python3
# @lcpr version=30305
#
# [378] 有序矩阵中第 K 小的元素
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        dp = []
        n = len(matrix[0])-1
        for i, data in enumerate(matrix):
            if not data:
                continue
            heapq.heappush(dp, (data[0], i, 0))
        
        for _ in range(k):
            val, i, idx = heapq.heappop(dp)
            if idx < n:
                heapq.heappush(dp, (matrix[i][idx+1], i, idx+1))
            
        return val
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    res = solution.kthSmallest(matrix, k)
    print(res)





#
# @lcpr case=start
# [[1,5,9],[10,11,13],[12,13,15]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[-5]]\n1\n
# @lcpr case=end

#

