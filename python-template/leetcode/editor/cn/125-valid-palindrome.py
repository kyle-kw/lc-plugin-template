#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30305
#
# [125] 验证回文串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 只遍历一次
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            t1, t2 = s[p1], s[p2]
            if not t1.isalnum():
                p1 += 1
                continue
            if not t2.isalnum():
                p2 -= 1
                continue
            
            if t1.lower() != t2.lower():
                return False
            p1 += 1
            p2 -= 1
        
        return True
    
    def isPalindromeOld(self, s: str) -> bool:
        # 先转换，再判断，遍历了两次
        new_s = "".join(char.lower() for char in s if char.isalnum())
        if not new_s or len(new_s) == 1:
            return True
        
        p1 = 0
        p2 = len(new_s) - 1
        while p1 < p2:
            if new_s[p1] != new_s[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

