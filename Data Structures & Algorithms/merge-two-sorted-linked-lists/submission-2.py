# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        n = ListNode()
        finalHead = n
        if not curr1 and not curr2:
            return None
        
        while True:
            
            if curr1 and curr2 and curr1.val<=curr2.val:
                n.val = curr1.val
                curr1 = curr1.next
            elif curr1 and curr2 and curr2.val<curr1.val:
                n.val = curr2.val
                curr2 = curr2.next
            elif curr1 == None and curr2:
                n.val = curr2.val
                curr2 = curr2.next
            elif curr2 == None and curr1:
                n.val = curr1.val
                curr1 = curr1.next

            if curr1 or curr2:
                temp = ListNode()
                n.next = temp
                n = n.next
            else:
                break

        return finalHead
    

            

        