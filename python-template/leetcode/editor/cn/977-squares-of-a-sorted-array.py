#
# @lc app=leetcode.cn id=977 lang=python3
# @lcpr version=30305
#
# [977] 有序数组的平方
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 只遍历一次，不需要排序。双指针，将绝对值大的数，添加到新数组
        p1 = 0
        p2 = len(nums) - 1
        nums_new = [0] * (p2+1)
        p = p2
        while p1 <= p2:
            if abs(nums[p1]) > abs(nums[p2]):
                nums_new[p] = nums[p1] * nums[p1]
                p1 += 1
            else:
                nums_new[p] = nums[p2] * nums[p2]
                p2 -= 1
            
            p -= 1
            
                
        return nums_new
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#

