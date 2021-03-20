from my_queue import Queue
from stackA import Stack
from random import randint


def random_queue(length=20):
    queue = Queue()
    for _ in range(length):
        queue.enqueue(randint(1, 10))
    return queue


def queue_reverser(queue):
    new_queue = Queue()
    stack = Stack()
    length = queue.length
    for _ in range(length):
        item = queue.dequeue()
        stack.push(item)
        queue.enqueue(item)
    for _ in range(length):
        new_queue.enqueue(stack.pop())
    return new_queue


def main():
    print('Queue reverser\n')
    q1 = random_queue(5)
    print(q1)

    q_rev = queue_reverser(q1)
    print(q_rev)
    print(q1)


if __name__ == '__main__':
    main()
