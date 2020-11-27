"""CS2515 Assignment 2 Submission.

Script Name: movieLib.py
Author: Conor Fox 119322236
"""

from functools import total_ordering
from bst import BSTNode


@total_ordering
class Movie:
    """Represents a single Movie."""

    def __init__(self, i_title, i_date=None, i_runtime=None):
        """Initialise a Movie Object."""
        self._title = i_title
        self._date = i_date
        self._time = i_runtime

    def __str__(self):
        """Return a short string representation of this movie."""
        return self._title

    def full_str(self):
        """Return a full string representation of this movie."""
        outstr = self._title + ": "
        outstr += str(self._date) + "; "
        outstr += str(self._time)
        return outstr

    def get_title(self):
        """Return the title of this movie."""
        return self._title

    def __eq__(self, other):
        """Return True if this movie has exactly same title as other."""
        if other._title == self._title:
            return True
        return False

    def __ne__(self, other):
        """Return False if this movie has exactly same title as other."""
        return not self._title == other._title

    def __lt__(self, other):
        """Return True if this movie is ordered before other.

        A movie is less than another if it's title is alphabetically before.
        """
        if other._title > self._title:
            return True
        return False


class MovieLib:
    """A movie library.

    Implemented using a BST.
    """

    def __init__(self):
        """Initialise a movie library."""
        self.bst = BSTNode(None)

    def __str__(self):
        """Return a string representation of the library.

        The string will be created by an in-order traversal.
        """
        return str(self.bst)

    def size(self):
        """Return the number of movies in the library."""
        return self.bst.size()

    def search(self, title):
        """Return Movie with matching title if there, or None.

        Args:
            title: a string representing a movie title.
        """
        output = self.bst.search(Movie(title))
        if output is not None:
            return output.get_title()

    def add(self, title, date, runtime):
        """Add a new movie to the library.

        Args:
            title - the title of the movie
            date - the date the movie was released
            runtime - the running time of the movie

        Returns:
            the movie file that was added, or None
        """
        return self.bst.add(Movie(title, date, runtime))

    def remove(self, title):
        """Remove and return the a movie object with the given title, if there.

        Args:
            title - the title of the movie to be removed
        """
        search_movie = Movie(title)
        return self.bst.remove(search_movie)
