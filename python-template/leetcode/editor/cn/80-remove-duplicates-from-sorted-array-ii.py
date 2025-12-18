#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30305
#
# [80] 删除有序数组中的重复项 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        p1 = 0
        p2 = 0
        cnt = 0
        n = len(nums)
        while p2 < n:
            if nums[p1] == nums[p2]:
                cnt += 1
            else:
                p1 = p2
                cnt = 1
            
            if cnt == 3:
                nums.pop(p2)
                cnt -= 1
                n -= 1
            else:
                p2 += 1
        
        return len(nums)
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [0,0,1,1,1,1,2,3,3]
    res = solution.removeDuplicates(nums)
    print(res)
    print(nums)




#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

