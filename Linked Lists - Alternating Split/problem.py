class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def append(head,data):
    if not head:
        head=Node(data,None)
        return head
    current=head
    while current.next:
        current=current.next
    current.next=Node(data,None)
    return head

def alternating_split(head):
    if not head or not head.next:
        raise ValueError()
    i=0
    first=None
    second=None
    current=head
    while current:
        if not i:
            first=append(first,current.data)
        else:
            second=append(second,current.data)
        current=current.next
        i=not i
    return Context(first,second)