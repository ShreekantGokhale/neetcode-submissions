# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        ls = []
        node = head
        while node.next:
            ls.append(node.val)
            node = node.next
        ls.append(node.val)
        head1 = ListNode(ls[-1])
        node1 = head1
        for i in list(reversed(ls))[1:]:
            node1.next = ListNode(i)
            node1 = node1.next
        return head1



