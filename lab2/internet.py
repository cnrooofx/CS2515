
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

    @content.setter
    def content(self, content):
        if isinstance(content, str):
            self._content = content
        else:
            raise TypeError("Content must be a string")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, Client):
            self._address = address
        else:
            raise TypeError("Address must reference a Client object")

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        if isinstance(sender, Client):
            self._sender = sender
        else:
            raise TypeError("Sender must reference a Client object")

    @property
    def path(self):
        return self._path

    def addToPath(self, path_update):
        self._path.enqueue(path_update)


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
