from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    i=0
    if node.data==None:
        raise ValueError()
    while True:
        if i==index:
            return node
        if node.next==None:
            raise ValueError()
        i+=1
        node=node.next