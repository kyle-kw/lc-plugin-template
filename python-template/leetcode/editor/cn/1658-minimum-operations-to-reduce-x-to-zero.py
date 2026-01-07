#
# @lc app=leetcode.cn id=1658 lang=python3
# @lcpr version=30305
#
# [1658] 将 x 减到 0 的最小操作数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        
        n = len(nums)
        p1 = 0
        p2 = 0
        sum_nums = 0
        max_len = float('-inf')
        while p2 < n:
            sum_nums += nums[p2]
            p2 += 1
            
            while sum_nums > target and p1 < p2:
                sum_nums -= nums[p1]
                p1 += 1
            
            if sum_nums == target:
                max_len = max(max_len, p2 - p1)
        
        return -1 if max_len == float('-inf') else n - max_len
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#

