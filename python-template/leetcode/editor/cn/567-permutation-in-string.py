#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=30305
#
# [567] 字符串的排列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        p1 = 0
        p2 = 0
        val = 0
        while p2 < len(s2):
            c = s2[p2]
            p2 += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    val += 1
                    
            while p2 - p1 >= len(s1):
                # 在这里判断是否找到了合法的子串
                if val == len(need):
                    return True
                d = s2[p1]
                p1 += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        val -= 1
                    window[d] -= 1

        # 未找到符合条件的子串
        return False
            
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

