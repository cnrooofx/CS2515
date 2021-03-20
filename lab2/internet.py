
from my_queue import Queue


class Packet:
    def __init__(self):
        self._content = ''
        self._address = None
        self._sender = None
        self._path = Queue()

    @property
    def content(self):
        return self._content

    @property
    def address(self):
        return self._address

    @property
    def sender(self):
        return self._sender

    @property
    def path(self):
        return self._path

    def addToPath(self, path_update):
        self._path.enqueue(path_update)
    
    def packet_received(self):
        return self._path.dequeue()


class Client:
    def __init__(self):
        self._queue = Queue()

    def send(self):
        return

    def recieve(self):
        return


class Router:
    def __init__(self):
        self._queue = Queue()

    def process(self):
        return


def main():
    pack = Packet()
    pack.content = 'hello'
    print(pack.content)


if __name__ == '__main__':
    main()
