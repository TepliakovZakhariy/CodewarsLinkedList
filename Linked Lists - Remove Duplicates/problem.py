class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return head
    current=head
    while current.next:
        if current.data==current.next.data:
            current.next=current.next.next
            continue
        current=current.next
    return head