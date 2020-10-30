"""Doubly Linked List."""


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
        self._head = DLLNode(None, None, None)
        self._tail = DLLNode(None, self._head, None)
        self._head.next = self._tail
        self._size = 0

    def _add_after(self, item, before):
        new_node = DLLNode(item, None, None)
        after = before.next
        new_node.next = after
        after.prev = new_node
        before.next = new_node
        new_node.prev = before
        self._size += 1

    def add_first(self, item):
        self._add_after(item, self._head)

    def add_last(self, item):
        last_node = self._tail.prev
        self._add_after(item, last_node)

    def add(self, pos, item):
        node = self._get_pos_node(pos)
        self._add_after(item, node)

    def _get_pos_node(self, pos):
        i = 0
        node = self._head.next
        while i < pos:
            node = node.next
            i += 1
        return node

    def get(self, pos):
        if pos < 0 or pos >= self._size:
            return None
        node = self._get_pos_node(pos)
        return node.item

    def get_first(self):
        if self._size == 0:
            return None
        first_node = self._head.next
        return first_node.element

    def get_last(self):
        if self._size == 0:
            return None
        last_node = self._tail.prev
        return last_node.element

    def replace(self, pos, item):
        node = self._get_pos_node(pos)
        node.element = item

    def _remove_node(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        node.element = None
        node.next = None
        node.prev = None

    def remove_first(self):
        if self._size > 0:
            self._remove_node(self._head.next)

    def remove_last(self):
        if self._size > 0:
            self._remove_node(self._tail.prev)

    def remove(self, pos):
        node = self._get_pos_node(pos)
        self._remove_node(node)


def main():
    new_list = DLLinkedList()
    # print(new_list._tail.prev)
    new_list.add_first('a')
    print(new_list.get_first())
    new_list.add_first('b')
    print(new_list.get_first())
    print(new_list.get_last())
    new_list.add_last('c')
    print(new_list.get_last())
    new_list.remove_first()
    print(new_list.get_first())
    print('Head:', new_list._head)
    print('Tail:', new_list._tail)
    print(new_list._head.next)
    print(new_list._tail.prev)


if __name__ == '__main__':
    main()
