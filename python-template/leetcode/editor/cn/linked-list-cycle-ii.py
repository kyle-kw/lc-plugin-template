#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30305
#
# [142] 环形链表 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            
            if p1 == p2:
                break
        
        if p2 is None or p2.next is None:
            return None
        
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

