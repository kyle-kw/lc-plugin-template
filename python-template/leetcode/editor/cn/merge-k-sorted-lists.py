#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30305
#
# [23] 合并 K 个升序链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val
    
    @staticmethod
    def create_head(nums: List[int]):
        if len(nums) == 0 or nums is None:
            return None
        head = ListNode(nums[0])
        p = head
        for i in range(1, len(nums)):
            p.next = ListNode(nums[i])
            p = p.next
        return head
    
    @staticmethod
    def print(head: 'ListNode'):
        p = head
        while p:
            arrow = ' -> ' if p.next else ''
            print(p.val, end=arrow)
            p = p.next
        print()

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy = ListNode(-1)
        p = dummy
        pd = []
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pd, (head.val, i, head))
        
        while pd:
            val, i, node = heapq.heappop(pd)
            p.next = node
            if node.next is not None:
                heapq.heappush(pd, (node.next.val, i, node.next))
            
            p = p.next
        
        return dummy.next
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    lists = [
        ListNode.create_head([1,4,5]),
        ListNode.create_head([1,3,4]),
        ListNode.create_head([2,6])
    ]
    res = solution.mergeKLists(lists)
    ListNode.print(res)
    





#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

