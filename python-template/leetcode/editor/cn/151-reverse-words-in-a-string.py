#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30305
#
# [151] 反转字符串中的单词
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        return ' '.join(self.reverse([o for o in s.strip().split(' ') if o]))
            
    
    def reverse(self, s: list):
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        
        return s
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#

