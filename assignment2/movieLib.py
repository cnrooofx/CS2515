"""CS2515 Assignment 2 Submission.

Script Name: movieLib.py
Author: Conor Fox 119322236
"""

from functools import total_ordering
from bst import BSTNode
from time import time


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
        self.bst = None

    def __str__(self):
        """Return a string representation of the library.

        The string will be created by an in-order traversal.
        """
        if self.bst is not None:
            return str(self.bst)

    def size(self):
        """Return the number of movies in the library."""
        if self.bst is None:
            return 0
        return self.bst.size()

    def search(self, title):
        """Return Movie with matching title if there, or None.

        Args:
            title: a string representing a movie title.
        """
        if self.bst is not None:
            return self.bst.search(Movie(title))

    def add(self, title, date, runtime):
        """Add a new movie to the library.

        Args:
            title - the title of the movie
            date - the date the movie was released
            runtime - the running time of the movie

        Returns:
            the movie file that was added, or None
        """
        add_movie = Movie(title, date, runtime)
        if self.bst is None:
            self.bst = BSTNode(add_movie)
            return add_movie
        return self.bst.add(add_movie)

    def remove(self, title):
        """Remove and return the a movie object with the given title, if there.

        Args:
            title - the title of the movie to be removed
        """
        if self.bst is not None:
            outcome = self.bst.remove(Movie(title))
            if self.bst.size() == 0:  # If tree is now empty
                self.bst = None  # Set reference to None
            return outcome

    def _testadd():
        library = MovieLib()
        library.add("Memento", "11/10/2000", 113)
        print(str(library))
        print("> adding Melvin and Howard")
        library.add("Melvin and Howard", "19/09/1980", 95)
        print(str(library))
        print("> adding a second version of Melvin and Howard")
        library.add("Melvin and Howard", "21/03/2007", 112)
        print(str(library))
        print("> adding Mellow Mud")
        library.add("Mellow Mud", "21/09/2016", 92)
        print(str(library))
        print("> adding Melody")
        library.add("Melody", "21/03/2007", 113)
        print(str(library))
        return library

    def _test():
        library = MovieLib()
        library.add("B", "b", 1)
        print("Library:", library)
        print("adding", "A")
        library.add("A", "a", 1)
        print("Library:", library)
        print("removing", "A")
        library.remove("A")
        print("Library:", library)
        print("adding", "C")
        library.add("C", "c", 1)
        print("Library:", library)
        print("removing", "C")
        library.remove("C")
        print("Library:", library)
        print("adding", "F")
        library.add("F", "f", 1)
        print("Library:", library)
        print("removing", "B")
        library.remove("B")
        print("Library:", library)
        print("adding", "C")
        library.add("C", "c", 1)
        print("Library:", library)
        print("adding", "D")
        library.add("D", "d", 1)
        print("Library:", library)
        print("adding", "C")
        library.add("C", "c", 1)
        print("Library:", library)
        print("adding", "E")
        library.add("E", "e", 1)
        print("Library:", library)
        print("removing", "B")
        library.remove("B")
        print("Library:", library)
        print("removing", "D")
        library.remove("D")
        print("Library:", library)
        print("removing", "C")
        library.remove("C")
        print("Library:", library)
        print("removing", "E")
        library.remove("E")
        print("Library:", library)
        print("adding", "L")
        library.add("L", "l", 1)
        print("Library:", library)
        print("adding", "H")
        library.add("H", "h", 1)
        print("Library:", library)
        print("adding", "I")
        library.add("I", "i", 1)
        print("Library:", library)
        print("adding", "G")
        library.add("G", "g", 1)
        print("Library:", library)
        print("removing", "L")
        library.remove("L")
        print("Library:", library)
        print("removing", "H")
        library.remove("H")
        print("Library:", library)
        print("removing", "I")
        library.remove("I")
        print("Library:", library)
        print("removing", "G")
        library.remove("G")
        print("Library:", library)


def build_library(filename):
    """Return a library of Movie files built from filename."""
    # open the file
    file = open(filename, "r", encoding="utf8")

    # create the library
    library = MovieLib()

    filecount = 0
    count = 0

    # now cycle through the  lines in the file, adding the movies to the
    # library
    for line in file:
        filecount += 1
        inputlist = line.split("\t")
        added = library.add(inputlist[0], inputlist[1], inputlist[2])
        if added is not None:
            count += 1

    # print out some info for sanity checking
    print("read a file with", filecount, "movies")
    print("Built a library with", count, "unique movie titles")
    return library


def build_and_search(file, searchlist):
    """Build and search tests for library."""
    print("Library for:", file)

    before = time()
    newlibrary = build_library(file)
    after = time()
    time_taken = after - before

    print("\tSize:", newlibrary.bst.size())
    print("\tTime to build: %fs" % time_taken)
    print("\tHeight of root node:", newlibrary.bst.height())
    print("\tProper BST?", newlibrary.bst._properBST())

    for searchitem in searchlist:
        print("Searching for:", searchitem)
        before = time()
        movie = newlibrary.search(searchitem)
        after = time()
        time_taken = after - before
        print("\t%s found in %fs" % (movie, time_taken))
        if movie:
            print("\t|_", movie.full_str())

    # newlibrary.bst._print_structure()
    # print(newlibrary.bst._BSTproperties())
    print("*-" * 25)


def main():
    """Test methods."""
    # MovieLib._testadd()
    # print('++++++++++')
    # MovieLib._test()

    searchlist = ["Wonder Woman", "Touch of Evil", "Delicatessen",
                  "Iron Man", "Avatar 2"]

    build_and_search("smallmovies.txt", searchlist)
    build_and_search("small_repeated_movies.txt", searchlist)
    build_and_search("movies.txt", searchlist)


if __name__ == "__main__":
    main()
