#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30305
#
# [234] 回文链表
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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        p = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        if p2:
            p1 = p1.next
        
        dummy = ListNode(-1)
        while p1:
            temp = p1
            p1 = p1.next
            
            temp.next = dummy.next
            dummy.next = temp
        new_p = dummy.next
        
        while p and new_p:
            if p.val != new_p.val:
                return False
            p = p.next
            new_p = new_p.next
        
        return True
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

