#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30305
#
# [82] 删除排序链表中的重复元素 II
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode(101)
        dummy2 = ListNode(-1)
        p1, p2 = dummy1, dummy2
        p = head
        while p:
            if (p.next and p.val == p.next.val) or p1.val == p.val:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            
            temp = p.next
            p.next = None
            p = temp
        
        return dummy2.next
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.create_head([1,2,2])
    res = solution.deleteDuplicates(head)
    ListNode.print(res)





#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#

