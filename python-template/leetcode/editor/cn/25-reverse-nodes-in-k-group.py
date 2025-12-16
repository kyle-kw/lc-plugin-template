#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30305
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        p1 = head
        p2 = head
        n = k - 1
        d = ListNode(-1)
        dt = d
        while p2:
            # 走k-1步
            reverse_fleg = True
            for _ in range(n):
                if p2:
                    p2 = p2.next
                else:
                    reverse_fleg = False
                    break
            
            # 判断是否有完整的k个节点
            if not reverse_fleg or not p2:
                break
            
            # 再走1步，并将前置节点断开
            temp = p2
            p2 = p2.next
            temp.next = None
            
            # 反转p1到断开的节点
            dummy = ListNode(-1)
            p = p1
            while p:
                t = p
                p = p.next
                
                t.next = dummy.next
                dummy.next = t
            
            # 将反转结果拼接到上次的结尾
            dt.next = dummy.next
            # 移动到反转之后的结尾
            while dt.next:
                dt = dt.next
            
            # 拼接后续节点
            dt.next = p2
            # 重新设置p1节点
            p1 = dt.next
        
        return d.next
            
            
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.create_head([1,2])
    k = 2
    res = solution.reverseKGroup(head, k)
    ListNode.print(res)





#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

