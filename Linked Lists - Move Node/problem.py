class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    moved_node=source.data
    source=source.next
    dest=push(dest,moved_node)
    return Context(source, dest)