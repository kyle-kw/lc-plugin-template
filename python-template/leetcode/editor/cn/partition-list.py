#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30305
#
# [86] 分隔链表
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1, p2 = dummy1, dummy2
        
        p = head
        while p is not None:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            
            temp = p.next
            p.next = None
            p = temp
        
        p1.next = dummy2.next
        
        return dummy1.next
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    l1 = ListNode.create_head([1,4,3,2,5,2])
    x = 3
    res = solution.partition(l1, x)
    ListNode.print(res)





#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

