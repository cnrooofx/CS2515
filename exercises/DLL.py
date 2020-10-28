# Exercise: implement a method to swap two adjacent nodes in the list.
# Exercise: implement a method to swap two arbitrary nodes in the list.
#
# Do this by
# (i) Leaving the DLLNodes as they are, and just swapping the items
# (ii) Leaving the items as they are, and swapping the next
#      and prev pointers for DLLNodes as required.

class DLLNode:
    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode


class DLLinkedList:
    def __init__(self):

    def add_after(self, item, before):

    def add_first(self, item):

    def add_last(self, item):

    def get_first(self):

    def get_last(self):

    def remove_node(self, node):

    def remove_first(self):

    def remove_last(self):
