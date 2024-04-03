def loop_size(head):
    slow=head
    fast=head
    count=0
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        
        if fast==slow:
            slow=head
            while True:
                slow=slow.next
                fast=fast.next
                if fast==slow:
                    count=0
                    while True:
                        count+=1
                        slow=slow.next
                        if fast==slow:
                            return count