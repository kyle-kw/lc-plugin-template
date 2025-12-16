#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30305
#
# [2] 两数相加
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode(-1)
        p = dummy
        temp = 0
        
        while p1 and p2:
            val = p1.val + p2.val + temp
            if val > 9:
                temp = 1
                val -= 10
            else:
                temp = 0
            p.next = ListNode(val)
            p = p.next 
            p1 = p1.next
            p2 = p2.next
        
        not_null_p = p1 if p1 else p2
        while not_null_p:
            val = not_null_p.val + temp
            if val > 9:
                temp = 1
                val -= 10
            else:
                temp = 0
            
            p.next = ListNode(val)
            p = p.next 
            not_null_p = not_null_p.next
        
        if temp == 1:
            p.next = ListNode(1)
        
        return dummy.next
                
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

#

