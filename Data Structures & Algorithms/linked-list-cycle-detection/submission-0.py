# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes = set()
        n = head
        while n and n.next:
            if n not in visitedNodes:
                visitedNodes.add(n)
                n = n.next
            else:
                return True
        
        return False



