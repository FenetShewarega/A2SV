# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lis=[]

        if not head:
            return None
        while head :
            lis.append(head.val)
            head=head.next
        lis.sort()
        # print(lis)
        h1 = target = ListNode(0)
        for i in range(len(lis)):
            target.next= ListNode(lis[i])
            target=target.next
        return h1 .next 
        