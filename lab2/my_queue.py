import time
import sys
from random import randint


class Queue:
    """ A queue using a python list, with internal wrap-around.

    Head and tail of the queue are maintained by internal pointers.
    When the list is full, a new bigger list is created.
    """

    def __init__(self):
        self._body = [None] * 10
        self._front = 0    # index of first element, but 0 if empty
        self._size = 0    # number of elements in the queue

    def __str__(self):
        output = '<-'
        if self._size > 0:
            i = self._front
            for _ in range(self._size):
                output += str(self._body[i]) + '-'
                i = (i + 1) % len(self._body)
        output += '<' + '     ' + self.summary()
        return output

    def get_size(self):
        """ Return the internal size of the queue. """
        return sys.getsizeof(self._body)

    def summary(self):
        """ Return a string summary of the queue. """
        return ('Front:' + str(self._front)
                + '; size:' + str(self._size))

    def _requeue(self):
        """ Grow/shrink the internal representation of the queue."""
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
        """ Add an item to the queue.

        Args:
            item - (any type) to be added to the queue.
        """
        if self._size == 0:
            self._body[0] = item      # assumes an empty queue has head at 0
            self._size = 1
        else:
            self._body[(self._front + self._size) % len(self._body)] = item
            self._size += 1
            if self._size == len(self._body):
                self._requeue()

    def dequeue(self):
        """ Return (and remove) the item in the queue for longest."""
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
            self._requeue()
        return item

    def length(self):
        """ Return the number of items in the queue. """
        return self._size

    def first(self):
        """ Return the first item in the queue. """
        if self._size == 0:
            return None
        return self._body[self._front]


def random_queue(length=20):
    queue = Queue()
    for _ in range(length):
        queue.enqueue(randint(1, 10))
    return queue


def basic_queue_test(q):
    """ Test basic functionality of a queue.

    Args:
        q - the Queue instance to tbe tested
    """
    q.enqueue(1)
    q.enqueue('a')
    q.dequeue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue('b')
    q.enqueue('c')
    q.dequeue()
    print('Should be: <-2-3-4-b-c-<')
    print('%s' % q)
    return q


def perf_comparison(n):
    """ Compare performance of different queue implementations.

    Args:
        n - the (int) number of items to be added to each queue during evaluations
    """

    print("Creating a queue of each type.")
    q0 = Queue()
    q1 = OldQueue()
    qlist = [q0, q1]

    print("Lengths of empty queues: ", end=" ")
    for q in qlist:
        print("", q.length(), end=" ")
    print()
    print("First basic enqueuing and dequeuing:")
    for i in range(len(qlist)):
        qlist[i].enqueue(1)
        qlist[i].enqueue('a')
        qlist[i].dequeue()
        qlist[i].enqueue(2)
        qlist[i].enqueue(3)
        qlist[i].enqueue(4)
        qlist[i].enqueue('b')
        qlist[i].enqueue('c')
        qlist[i].dequeue()
        print('q', i, ':', qlist[i])

    print('enqueuing n items, then dequeuing n in each queue:')
    for i in range(len(qlist)):
        start_time = time.perf_counter()
        for j in range(n):
            qlist[i].enqueue(1)
        for j in range(n):
            qlist[i].dequeue()
        end_time = time.perf_counter()
        print(i, 'took', end_time - start_time,
              'and has size', qlist[i].get_size(),
              'but length', qlist[i].length())

    print('now starting again, and maintaining a list of size 20 through',
          'n operations')
    qlist[0] = Queue()
    qlist[1] = OldQueue()
    for i in range(len(qlist)):
        start_time = time.perf_counter()
        for j in range(20):
            qlist[i].enqueue(1)
        for j in range(n):
            qlist[i].enqueue(1)
            qlist[i].dequeue()
        end_time = time.perf_counter()
        print(i, 'took', end_time - start_time,
              'and has size', qlist[i].get_size(),
              'but length', qlist[i].length())


def my_tests():
    print('Tests')
    q = Queue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    # print(q._body)
    # q.dequeue()
    # q.dequeue()
    # print(q._body)
    q.enqueue('e')
    q.enqueue('f')
    q.enqueue('g')
    q.enqueue('h')
    # print(q._body)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    # print(q._body)
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    # print(q._body)
    q.enqueue('a')
    q.enqueue('b')
    # q.enqueue('P')
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    q.enqueue('e')
    q.enqueue('f')
    q.enqueue('g')
    q.enqueue('h')
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    q.enqueue('e')
    q.enqueue('f')
    q.enqueue('g')
    q.enqueue('h')
    print(q._body)
    print(q)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q._body)
    print(q.length())
    print(q.dequeue())
    print(q.length())
    print(q)

    # q = basic_queue_test(q)
    # q = basic_queue_test(q)
    # q = basic_queue_test(q)
    # q = basic_queue_test(q)
    # q = basic_queue_test(q)
    # print('Elements: %d, Body Length: %d, Size: %d' % (q.length(), len(q._body), q.get_size()))
    # print((q.length() / len(q._body)) < 0.25)
    # for i in range(16):
    #     q.dequeue()
    # print(q._body)
    # print('Elements: %d, Body Length: %d, Size: %d' % (q.length(), len(q._body), q.get_size()))
    # print((q.length() / len(q._body)) < 0.25)

    # q = random_queue(9)
    # print(q)
    # print(q._body)
    # for i in range(12):
    #     q.dequeue()
    #     print(q._body)
    #     print('Head:', q._front)  # , 'Tail:', q._tail)
    # print(q)
    # for i in range(10):
    #     q.enqueue(randint(1, 10))
    #     print(q._body)
    #     print('Head:', q._front)  # , 'Tail:', q._tail)
    # print(q)
    # print(q._body)



def main():
    perf_comparison(1000000)
    # my_tests()


if __name__ == '__main__':
    main()
