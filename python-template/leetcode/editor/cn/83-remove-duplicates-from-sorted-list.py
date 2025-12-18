#
# @lc app=leetcode.cn id=83 lang=python3
# @lcpr version=30305
#
# [83] 删除排序链表中的重复元素
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
        p1 = head
        p2 = head
        while p2:
            if p1.val != p2.val:
                p1.next = p2
                p1 = p1.next
            
            p2 = p2.next
        if p1:
            p1.next = None
        return head
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.create_head([1,1,2,3,3])
    res = solution.deleteDuplicates(head)
    ListNode.print(res)




#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#

