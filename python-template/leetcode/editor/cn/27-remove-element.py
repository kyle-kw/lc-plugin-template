#
# @lc app=leetcode.cn id=27 lang=python3
# @lcpr version=30305
#
# [27] 移除元素
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1
                
            p2 += 1
        
        return p1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [3, 3]
    res = solution.removeElement(nums, 3)
    print(res)
    print(nums)





#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

