#
# @lc app=leetcode.cn id=373 lang=python3
# @lcpr version=30305
#
# [373] 查找和最小的 K 对数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        dp = []
        n1 = len(nums1)
        n2 = len(nums2) - 1
        for i in range(n1):
            heapq.heappush(dp, (nums1[i]+nums2[0], [nums1[i], nums2[0]], i, 0))
        
        res = []
        for _ in range(k):
            val, one, i, j = heapq.heappop(dp)
            res.append(one)
            if j < n2:
                heapq.heappush(dp, (nums1[i]+nums2[j+1], [nums1[i], nums2[j+1]], i, j+1))
        
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#

