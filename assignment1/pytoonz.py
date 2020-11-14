"""CS2515 Assignment 1 Submission.

Script Name: pytoonz.py
Author: Conor Fox 119322236
"""


class DLLNode:
    """Node for an item in a Doubly Linked List."""

    def __init__(self, item, prevnode, nextnode):
        """Create a DLLNode object."""
        self.item = item
        self.next = nextnode
        self.prev = prevnode


class Track:
    """Track object to be used in a PyToonz playlist."""

    def __init__(self, name, artiste, timesplayed=0):
        """Create a Track object.

        Args:
            name (str): The name of the Track
            atriste (str): The atriste of the Track
            timesplayed (int): Counter for track plays (Default: 0)
        """
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed

    def __str__(self):
        """Return a string representation of the track."""
        s = '{}; {} ({})'.format(self._name, self._artiste, self._timesplayed)
        return s

    def get_name(self):
        """Return the name of the track."""
        return self._name

    def get_artiste(self):
        """Return the name of the artiste."""
        return self._artiste

    def play(self):
        """Play the track (Return string and increment it's play count)."""
        self._timesplayed += 1
        return 'Playing: ' + str(self)


class PyToonz:
    """Class for a PyToonz playlist."""

    def __init__(self):
        """Create a PyToonz object."""
        self._head = DLLNode(None, None, None)
        self._tail = DLLNode(None, self._head, None)
        self._head.next = self._tail
        self._selected = None
        self._length = 0

    def __str__(self):
        """Return a string representation of the playlist."""
        s_list = ['Playlist:']
        if self._length > 0:
            i = 0
            track = self._head.next
            while i < self._length:
                item = str(track.item)
                if track is self._selected:
                    item = '--> ' + item
                s_list.append(item)
                track = track.next
                i += 1
        return '\n'.join(s_list)

    def length(self):
        """Return the length of the playlist."""
        return self._length

    def add_track(self, track):
        """Add a new track to the end of the playlist."""
        self._add_track_node(track, self._tail.prev)

    def get_current(self):
        """Return the currently selected track."""
        if self._selected is None:
            return None
        return 'Current track: ' + str(self._selected.item)

    def add_after(self, track):
        """Add a new track after the currently selected track."""
        if self._selected is None:
            self.add_track(track)  # If there is no selected track, add to end
        else:
            self._add_track_node(track, self._selected)

    def next_track(self):
        """Select the next track in the playlist."""
        if self._selected is not None:
            if self._selected.next is self._tail:  # If the next track is tail
                self._selected = self._head.next  # Move current to first track
            else:
                self._selected = self._selected.next  # Set to the next track

    def prev_track(self):
        """Select the previous track in the playlist."""
        if self._selected is not None:
            if self._selected.prev is self._head:  # If the prev track is head
                self._selected = self._tail.prev  # Move current to last track
            else:
                self._selected = self._selected.prev  # Set to previous track

    def reset(self):
        """Set current track to first one in the playlist."""
        if self._length != 0:
            self._selected = self._head.next

    def play(self):
        """Play the currently selected track."""
        if self._selected is None:
            print('Error - No track currently selected to play.')
        else:
            print(self._selected.item.play())

    def remove_current(self):
        """Remove the currently selected track."""
        if self._selected is not None:
            previous = self._selected.prev  # Track before removed one
            next = self._selected.next   # Track after removed one

            previous.next = next
            next.prev = previous

            self._selected.item = None
            self._selected.next = None
            self._selected.prev = None

            self._length -= 1
            if self._length == 0:
                self._selected = None
            elif next is self._tail:  # If the item was the last in the list
                self._selected = previous  # Set the selection to the last item
            else:
                self._selected = next  # Set to item after the removed one

    def _add_track_node(self, track, previous):
        new_node = DLLNode(track, None, None)
        next = previous.next     # Next track in the playlist

        new_node.next = next   # Link new node to following node
        next.prev = new_node
        previous.next = new_node  # Link new node to preceding node
        new_node.prev = previous

        if self._length == 0:  # If the length is 0, it is the first track
            self._selected = new_node  # Set the new node as selected
        self._length += 1


def test():
    """My test methods for PyToonz."""
    print('-' * 25)
    print('Track')
    print('-' * 25)
    t1 = Track('Track 1', 'Artist 1')
    t2 = Track('Track 2', 'Artist 1')
    t3 = Track('Track 3', 'Artist 2')
    print(t1)
    print(t2)
    print(t3)
    t1.play()
    t1.play()
    t1.play()
    t1.play()
    print(t1)
    print(t2.get_artiste())
    print(t3.get_name())
    t1 = Track('Track 1', 'Artist 1')
    print('-' * 25)
    print('PyToonz')
    print('-' * 25)
    playlist = PyToonz()
    print(playlist)
    print('-' * 25)
    print('Adding Tracks')
    print('-' * 25)
    playlist.add_track(t1)
    playlist.add_track(t2)
    playlist.add_track(t3)
    print(playlist)
    t4 = Track('Track 4', 'Artist 3')
    playlist.next_track()
    playlist.add_after(t4)
    print(playlist)
    print('-' * 25)
    print('Prev & Next')
    print('-' * 25)
    print(playlist)
    playlist.next_track()
    playlist.next_track()
    print(playlist)
    playlist.next_track()
    print(playlist)
    playlist.prev_track()
    print(playlist)
    print('-' * 25)
    print('Playing')
    print('-' * 25)
    playlist.play()
    playlist.play()
    playlist.play()
    playlist.next_track()
    playlist.play()
    playlist.next_track()
    playlist.play()
    print(playlist)
    print('-' * 25)
    print('Removing Tracks')
    print('-' * 25)
    playlist.reset()
    print(playlist)
    for i in range(10):
        playlist.remove_current()
    print(playlist)
    playlist.add_track(t1)
    playlist.add_track(t2)
    playlist.add_track(t3)


if __name__ == '__main__':
    test()
