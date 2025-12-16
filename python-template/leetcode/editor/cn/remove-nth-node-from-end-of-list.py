#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30305
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        dummy1.next = head
        dummy2.next = head
        p = dummy2

        for _ in range(n):
            dummy1 = dummy1.next
        
        while dummy1 is not None and dummy1.next is not None:
            dummy1 = dummy1.next
            dummy2 = dummy2.next
        
        temp = dummy2.next
        dummy2.next = dummy2.next.next
        temp.next = None
        
        return p.next
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.create_head([1,2])
    n = 2
    res = solution.removeNthFromEnd(head, n)
    ListNode.print(res)





#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

