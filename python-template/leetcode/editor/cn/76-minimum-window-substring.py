#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30305
#
# [76] 最小覆盖子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        window = {}
        
        p1 = 0
        p2 = 0
        val = 0
        start = 0
        length = float('inf')

        while p2 < len(s):
            c = s[p2]
            p2 += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    val += 1
            
            while val == len(need):
                if (p2 - p1) < length:
                    start = p1
                    length = p2 - p1
                
                c = s[p1]
                p1 += 1
                if c in need:
                    if window[c] == need[c]:
                        val -= 1
                    window[c] -= 1
            
        return "" if length == float('inf') else s[start: start+length]
    
    def minWindowOld(self, s: str, t: str) -> str:
        # 超时
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        n = len(s)
        m = len(t)
        p1 = 0
        p2 = 0
        min_s = ""
        while p2 < n:
            p2 += 1
            if p2 - p1 < m:
                continue
            
            ts = s[p1: p2] 
            
            window = {}
            for c in ts:
                window[c] = window.get(c, 0) + 1
            
            all_c = True
            for k, v in need.items():
                if window.get(k, 0) < v:
                    all_c = False
                    break
            
            if not all_c:
                continue
            
            while p1 < p2:
                p1 += 1
                if p2 - p1 >= m:
                    
                    ts = s[p1: p2] 
                    window = {}
                    for c in ts:
                        window[c] = window.get(c, 0) + 1
                    
                    all_c = True
                    for k, v in need.items():
                        if window.get(k, 0) < v:
                            all_c = False
                            break
                else:
                    all_c = False
                    
                if not all_c:
                    p1 -= 1
                    t_min_s = s[p1: p2]
                    if not min_s or (len(t_min_s) < len(min_s)):
                        min_s = t_min_s
                    break
        
        return min_s
            

            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    s = "ADOBECODEBANC"

    t = "ABC"
    res = solution.minWindow(s, t)
    print(res)





#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

