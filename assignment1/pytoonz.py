"""CS2515 Assignment 1 Submission.

Script Name: pytoonz.py
Author: Conor Fox 119322236
"""


class DLNode:
    """Node for an item in a Doubly Linked List."""

    def __init__(self, item, prevnode, nextnode):
        """Create a DLNode object."""
        self.item = item
        self.next = nextnode
        self.prev = prevnode


class Track:
    """Track object to be used in a PyToonz playlist."""

    def __init__(self, name, artiste, timesplayed=0):
        """Create a Track object."""
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed

    def __str__(self):
        """Return a string representation of the track."""
        s = "{}; {} ({})".format(self._name, self._artiste, self._timesplayed)
        return s

    def get_name(self):
        """Return the name of the track."""
        return self._name

    def get_artiste(self):
        """Return the name of the artiste."""
        return self._artiste

    def play(self):
        """Play the track and increment it's play count."""
        self._timesplayed += 1
        return self


class PyToonz:
    """Class for a PyToonz playlist."""

    def __init__(self):
        """Create a PyToonz object."""
        self._head = DLNode(None, None, None)
        self._tail = DLNode(None, self._head, None)
        self._head.next = self._tail
        self._length = 0
        self._current = None

    def __str__(self):
        """Return a string representation of the playlist."""
        s = 'Playlist:'
        if self._length > 0:
            i = 0
            node = self._head.next
            while i < self._length:
                if node == self._current:
                    s += '\n--> '
                else:
                    s += '\n'
                s += str(node.item)
                node = node.next
                i += 1
        return s

    def length(self):
        """Return the length of the playlist."""
        return self._length

    def add_track(self, track):
        """Add track to the end of the playlist."""
        self._add_track_node(track, self._tail.prev)

    def get_current(self):
        """Return the currently selected track."""
        return self._current.item

    def add_after(self, track):
        """Add a new track after the current track."""
        self._add_track_node(track, self._current)

    def next_track(self):
        """Select the next track in the playlist."""
        if self._current.next != self._tail:
            self._current = self._current.next
        else:
            self._current = self._head.next

    def prev_track(self):
        """Select the previous track in the playlist."""
        if self._current.next != self._head:
            self._current = self._current.prev
        else:
            self._current = self._tail.prev

    def reset(self):
        """Remove all tracks from the playlist."""
        pass

    def play(self):
        """Play the currently selected track."""
        if self._current is not None:
            self._current.item.play()

    def remove_current(self):
        """Remove the current track."""
        self._remove_track_node(self._current)

    def _add_track_node(self, track, before):
        new_node = DLNode(track, None, None)  # Create new node object
        after = before.next     # Get the next track in the playlist
        new_node.next = after   # Link the new track into the playlist
        after.prev = new_node
        before.next = new_node
        new_node.prev = before
        if self._length == 0:   # If it's the first track, set it to current
            self._current = new_node
        self._length += 1       # Increment the playlist length

    def _remove_track_node(self, track):
        before = self._current.prev  # Track after removed one
        after = self._current.next   # Track before removed one
        before.next = after          # Link the two tracks
        after.prev = before
        self._current.element = None  # Set the node at current to None
        self._current.next = None
        self._current.prev = None
        self._current = after        # Set the current pointer to next track


def test():
    """My test methods for PyToonz."""
    print("------------\nTrack\n------------")
    t1 = Track('Track 1', 'Artist 1')
    t2 = Track('Track 2', 'Artist 1')
    t3 = Track('Track 3', 'Artist 2')
    print(t1)
    print(t2)
    print(t3)
    print(t1.play())


def basic_test():
    """Sample test method for assignment."""
    playlist = PyToonz()
    t1 = Track("Looking for me", "Paul Woolford and Diplo/Lomax", 0)
    playlist.add_track(t1)
    t2 = Track("Giants", "Dermot Kennedy", 0)
    playlist.add_track(t2)
    t3 = Track("Holy", "Justin Bieber Ft Chance", 0)
    playlist.add_track(t3)
    print(playlist)
    print(playlist.play())
    playlist.next_track()
    print(playlist.get_current())
    playlist.prev_track()
    print(playlist.remove_current())
    print(playlist)
    t4 = Track("Lemonade", "Internet Money / Gunna / Toliver", 0)
    playlist.add_track(t4)
    playlist.next_track()
    print(playlist.play())
    print(playlist)


if __name__ == '__main__':
    # test()
    basic_test()
