"""Class for a Queue ADT."""

import sys


class Queue:
    """A queue using a python list, with internal wrap-around.

    Attributes:
        _body: List that represents the queue body (protected)
        _front: Index of the front item in the queue (protected)
        _size: Number of elements in the queue (protected)
    """

    def __init__(self):
        """Construct a queue object."""
        self._body = [None] * 10
        self._front = 0    # index of first element, but 0 if empty
        self._size = 0    # number of elements in the queue

    def __str__(self):
        """Return a string representation of the queue."""
        output = '<-'
        if self._size > 0:
            i = self._front
            for _ in range(self._size):
                output += str(self._body[i]) + '-'
                i = (i + 1) % len(self._body)
        output += '<' + '     ' + self._summary()
        return output

    def _get_size(self):
        """Return the internal size of the queue."""
        return sys.getsizeof(self._body)

    def _summary(self):
        """Return a string summary of the queue."""
        return ('Front:' + str(self._front)
                + '; size:' + str(self._size))

    def __requeue(self):
        """Grow/shrink the internal representation of the queue."""
        oldbody = self._body
        oldlength = len(self._body)
        self._body = [None] * (2*self._size)
        oldpos = self._front
        pos = 0
        for _ in range(self._size):
            self._body[pos] = oldbody[oldpos]
            oldbody[oldpos] = None
            pos += 1
            oldpos = (oldpos + 1) % oldlength
        self._front = 0
        self._tail = self._size

    def enqueue(self, item):
        """Add an item to the queue.

        Args:
            item (any type): to be added to the queue.
        """
        if self._size == 0:
            self._body[0] = item      # assumes an empty queue has head at 0
            self._size = 1
        else:
            self._body[(self._front + self._size) % len(self._body)] = item
            self._size += 1
            if self._size == len(self._body):
                self.__requeue()

    def dequeue(self):
        """Return (and remove) the item in the queue for longest."""
        if self._size == 0:
            return None
        item = self._body[self._front]
        self._body[self._front] = None
        if self._size == 1:
            self._front = 0
            self._size = 0
        else:
            self._front = (self._front + 1) % len(self._body)
            self._size -= 1
        if (self._size / len(self._body)) < 0.25:
            self.__requeue()
        return item

    @property
    def length(self):
        """Return the number of items in the queue."""
        return self._size

    @property
    def first(self):
        """Return the first item in the queue."""
        if self._size == 0:
            return None
        return self._body[self._front]
