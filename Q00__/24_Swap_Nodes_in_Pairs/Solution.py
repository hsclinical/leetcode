# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            newHead = head.next
            cnt = 0
            while True:
                if cnt % 2 == 0:
                    if head == None or head.next == None:
                        break
                    else:
                        tmpHead = head.next
                        head.next = tmpHead.next
                        tmpHead.next = head
                else:
                    if head.next == None or head.next.next == None:
                        break
                    else:
                        tmpHead = head.next
                        head.next = tmpHead.next
                        head = tmpHead
                cnt += 1

            return newHead