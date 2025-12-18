#
# @lc app=leetcode.cn id=167 lang=python3
# @lcpr version=30305
#
# [167] 两数之和 II - 输入有序数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            temp = numbers[p1]+numbers[p2]
            if temp == target:
                return [p1+1, p2+1]
            elif temp < target:
                p1 += 1
            else:
                p2 -= 1
        
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#

