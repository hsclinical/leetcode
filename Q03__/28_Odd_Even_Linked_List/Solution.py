# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None or head.next.next == None:
            return head

        firstOdd = head
        firstEven = head.next
        cnt = 0
        while True:
            if cnt % 2 == 0:
                lastOdd = head
            cnt += 1

            tmpHead = head.next
            if tmpHead == None:
                break
            head.next = tmpHead.next
            head = tmpHead

        lastOdd.next = firstEven
        return firstOdd