#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30305
#
# [26] 删除有序数组中的重复项
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p1 = 0
        p2 = 0
        while p2 < n:
            # 若p1和p2的值相同，则p2走一步
            if nums[p1] == nums[p2]:
                p2 += 1
                continue
            
            # 否则替换p2和p1+1的值
            p1 += 1
            nums[p1], nums[p2] = nums[p2], nums[p1]
            
            # 结束p2走一步
            p2 += 1
        
        # 遍历完成之后，p1+1就是非重复的数量
        return p1 + 1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [1,1,2]
    res = solution.removeDuplicates(nums)
    print(res)
    print(nums)




#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

