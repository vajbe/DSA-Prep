#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

  def removeNthFromEnd(self, head: Optional[ListNode],
                       n: int) -> Optional[ListNode]:
    if head is None:
      return head
    if head.next is None:
      return None
    if n < 1:
      return head
    node = head
    index = 0
    while node:
      index += 1
      node = node.next
    removeIndex = index - n

    node = head
    while removeIndex > 1:
      node = node.next
      removeIndex -= 1

    if node == head and removeIndex == 0:
      head = head.next
      return head

    nextNode = node.next
    node.next = nextNode.next
    nextNode.next = None
    return head


#[1,2],        1
#[1,2],        2
#[1],          1
#[1,2,3,4,5]   3
