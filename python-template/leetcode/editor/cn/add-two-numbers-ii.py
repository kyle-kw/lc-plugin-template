#
# @lc app=leetcode.cn id=445 lang=python3
# @lcpr version=30305
#
# [445] 两数相加 II
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
        nums1 = []
        nums2 = []
        while p1:
            nums1.append(p1.val)
            p1 = p1.next
        
        while p2:
            nums2.append(p2.val)
            p2 = p2.next
        
        dummy = ListNode(-1)
        temp = 0
        while nums1 or nums2 or temp > 0:
            val = temp
            if nums1:
                val += nums1.pop()
            
            if nums2:
                val += nums2.pop()
            
            temp = val // 10
            val = val % 10
            newNode = ListNode(val)
            newNode.next = dummy.next
            dummy.next = newNode
            
        return dummy.next
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here





#
# @lcpr case=start
# [7,2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

#

