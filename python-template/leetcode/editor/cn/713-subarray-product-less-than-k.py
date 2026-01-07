#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30305
#
# [713] 乘积小于 K 的子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        length = len(nums)
        
        p1 = 0
        p2 = 0
        cnt = 0
        mut_res = 1
        while p2 < length:
            mut_res *= nums[p2]
            p2 += 1
            
            while p1 < p2 and mut_res >= k:
                mut_res //= nums[p1]
                p1 += 1

            cnt += p2 - p1
        
        
        return cnt
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

