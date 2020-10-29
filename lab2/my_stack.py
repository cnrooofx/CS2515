"""Class for a Stack ADT using linked list."""


class SLNode:
    """A node to be used in a Singly Linked List."""

    def __init__(self, item, next_node):
        """Construct an SLNode object."""
        self.element = item
        self.next = next_node


class Stack:
    """A stack using a linked list.

    Attributes:
        _first: First element node in the stack (protected)
        _size: Number of elements in the stack (protected)
    """

    def __init__(self):
        """Construct the stack class."""
        self._first = None
        self._size = 0

    def push(self, element):
        """Place element onto the top of the stack."""
        self._first = SLNode(element, self._first)
        self._size += 1

    def pop(self):
        """Remove and return the top element of the stack."""
        if self._size == 0:
            return None
        item = self._first.element
        self._first = self._first.next
        self._size -= 1
        return item

    @property
    def top(self):
        """Return but don't remove the top element of the stack."""
        if self._size == 0:
            return None
        return self._first.element

    @property
    def length(self):
        """Return the number of elements on the stack."""
        return self._size

    def __str__(self):
        """Return a string representation of the stack."""
        output = ''
        next = self._first
        for i in range(self._size):
            output = str(next.element) + '-' + output
            next = next.next
        output = '|-' + output + '->'
        return output
