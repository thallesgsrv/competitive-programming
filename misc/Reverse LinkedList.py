class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

prev = None
curr = head

while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

print(prev.val)
print(prev.next.val) 
print(prev.next.next.val)
print(prev.next.next.next.val)
print(prev.next.next.next.next.val)

# This code is reversing a singly linked list. It initializes three pointers: `prev`, `curr`, and `next_node`. The `prev` pointer starts as `None`, the `curr` pointer starts at the head of the list, and the `next_node` pointer is used to temporarily store the next node in the list during the reversal process. The code iterates through the linked list, reversing the direction of the `next` pointers until it reaches the end of the list. Finally, it prints the values of the reversed linked list starting from the new head (which was originally the tail).
