#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30305
#
# [206] 反转链表
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = head
        while p:
            temp = p
            p = p.next
            
            temp.next = dummy.next
            dummy.next = temp
            
        return dummy.next
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

