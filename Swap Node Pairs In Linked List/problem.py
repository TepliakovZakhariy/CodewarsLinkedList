from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    curr=head
    next=head.next
    curr.next=swap_pairs(next.next)
    next.next=curr
    return next