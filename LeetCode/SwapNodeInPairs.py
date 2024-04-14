#https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        tempNode = head.next
        prev = None
        node = head

        while node:
            newNode = node.next
            if(newNode):               
                node.next = newNode.next
                newNode.next = node
                if prev is not None:
                    prev.next = newNode
                prev = node
            node = node.next
        return tempNode