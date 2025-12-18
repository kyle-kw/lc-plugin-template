#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30305
#
# [75] 颜色分类
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        
        p1 = 0
        p2 = 0
        p3 = n - 1
        while p2 <= p3:
            if nums[p2] == 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                # 前面的值都判断过了，所以p2走一步
            elif nums[p2] == 2:
                nums[p3], nums[p2] = nums[p2], nums[p3]
                p3 -= 1
                # 因为后面的值还没有判断，需要p2不需要动
                continue
            p2 += 1
    
    def sortColorsOld(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        
        p1 = 0
        p2 = n - 1
        # 尾指针移动到非2的位置
        while p2 >= 0 and nums[p2] == 2:
            p2 -= 1
        
        # 先把2移动到最后
        while p1 < p2:
            if nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
        
        # 继续尾指针移动到非2的位置
        while p2 >= 0 and nums[p2] == 2:
            p2 -= 1
        
        # 先把1移动到后面
        p1 = 0
        while p1 < p2:
            if nums[p1] == 1:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [2,0,2,1,1,0]
    solution.sortColors(nums)
    print(nums)




#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

