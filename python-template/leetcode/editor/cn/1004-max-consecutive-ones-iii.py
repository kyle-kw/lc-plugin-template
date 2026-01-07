#
# @lc app=leetcode.cn id=1004 lang=python3
# @lcpr version=30305
#
# [1004] 最大连续1的个数 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # p1 = 0
        # p2 = 0
        # replace_num = k
        # replace_idx = []
        # max_length = 0
        
        # while p2 < len(nums):
        #     one = nums[p2]
        #     if one == 1:
        #         p2 += 1
            
        #     max_length = max(max_length, p2 - p1+1)
            
        #     while p1 < p2 and replace_num == 0:
        #         if p1 in replace_idx:
        #             replace_num += 1
        #             replace_idx.remove(p1)
        #         p1 += 1
                
        
        # return max_length
        left = 0
        window_one_count = 0
        res = 0
        for right in range(len(nums)):
            # 右指针往右移, 先统计当前区间所有的1(扩大窗口)
            if nums[right] == 1:
                window_one_count += 1
            
            # 计算当前区间的长度减去1的数量,就是要保留所有1要反转的数量
            # 当要反转的数量大于给定的反转数量时,左边指针就开始右移(缩小窗口)
            while right - left + 1 - window_one_count > k:
                if nums[left] == 1:
                    window_one_count -= 1
                left += 1
            
            # 更新最大符合条件的数量
            res = max(res, right - left + 1)
        
        return res
            
            
                
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#

