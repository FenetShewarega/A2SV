# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        new = ListNode(0)
        new.next = head
        
        curr, prev = head, new
        while curr:
         
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
        
            if prev.next == curr:
                prev = prev.next
                curr = curr.next

            else:
                prev.next = curr.next
                curr = prev.next
        return new.next