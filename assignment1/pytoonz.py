"""CS2515 Assignment 1 Submission.

Script Name: pytoonz.py
Author: Conor Fox 119322236
"""


class Track:
    def __init__(self, name, artiste):
        self._name = name
        self._artiste = artiste
        self._timesplayed = 0

    def __str__(self):
        s = "{}; {} ({})".format(self._name, self._artiste, self._timesplayed)
        return s

    def get_name(self):
        return self._name

    def get_artiste(self):
        return self._artiste

    def play(self):
        self._timesplayed += 1
        return self


def test():
    print("------------\nTrack\n------------")
    t1 = Track('Track 1', 'Artist 1')
    t2 = Track('Track 2', 'Artist 1')
    t3 = Track('Track 3', 'Artist 2')
    print(t1)
    print(t2)
    print(t3)
    print(t1.play())


if __name__ == '__main__':
    test()
