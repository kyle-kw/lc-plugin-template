#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30305
#
# [92] 反转链表 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        p1 = dummy
        p2 = dummy
        p3 = head
        for _ in range(left-1):
            p1 = p1.next
            p2 = p2.next
        
        p2 = p2.next
        
        for _ in range(right-1):
            p3 = p3.next
        
        temp = p3
        p3 = p3.next
        temp.next = None
        
        dummy2 = ListNode(-1, p3)
        tp2 = p2
        while tp2:
            temp = tp2
            tp2 = tp2.next
            
            temp.next = dummy2.next
            dummy2.next = temp
        
        p1.next = dummy2.next
        
        return dummy.next
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

