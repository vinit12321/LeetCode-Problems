# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=head
        j=head
        temp=head
        if head.next is None:
            return None
        cnt=0
        while (temp):
            cnt+=1
            temp=temp.next

        for _ in range(n):
            
            if j is None:
                return -1
            j=j.next
        
        if cnt==n:
            return head.next

        prev=head  
        while (j is not None and i is not None):
            prev=i
            i=i.next
            j=j.next
        print(i,j)
        if i is not None and i.next is not None:
            new_node=i
            prev.next=new_node.next
        elif i is not None and i.next is None:
            prev.next=None
        return head


        
        