from movieLib import MovieLib
from time import time


def build_library(filename):
    """ Return a library of Movie files built from filename """

    # open the file
    file = open(filename, 'r', encoding="utf8")

    # create the library
    library = MovieLib()

    filecount = 0
    count = 0

    # now cycle through the  lines in the file, adding the movies to the
    # library
    for line in file:
        filecount += 1
        inputlist = line.split('\t')
        added = library.add(inputlist[0], inputlist[1], inputlist[2])
        if added is not None:
            count += 1

    # print out some info for sanity checking
    print("read a file with", filecount, "movies")
    print("Built a library with", count, "unique movie titles")
    return library


def test():
    library = MovieLib()
    library.add("B", "b", 1)
    print('Library:', library)
    print('adding', "A")
    test_add = library.add("A", "a", 1)
    print(test_add.full_str(), "*" * 25)
    print('Library:', library)
    print('removing', "A")
    library.remove("A")
    print('Library:', library)
    print('adding', "C")
    library.add("C", "c", 1)
    print('Library:', library)
    print('removing', "C")
    library.remove("C")
    print('Library:', library)
    print('adding', "F")
    library.add("F", "f", 1)
    print('Library:', library)
    print('removing', "B")
    library.remove("B")
    print('Library:', library)
    print('adding', "C")
    library.add("C", "c", 1)
    print('Library:', library)
    print('adding', "D")
    library.add("D", "d", 1)
    print('Library:', library)
    print('adding', "C")
    library.add("C", "c", 1)
    print('Library:', library)
    print('adding', "E")
    library.add("E", "e", 1)
    print('Library:', library)
    print('removing', "B")
    library.remove("B")
    print('Library:', library)
    print('removing', "D")
    library.remove("D")
    print('Library:', library)
    print('removing', "C")
    library.remove("C")
    print('Library:', library)
    print('removing', "E")
    library.remove("E")
    print('Library:', library)
    print('adding', "L")
    library.add("L", "l", 1)
    print('Library:', library)
    print('adding', "H")
    library.add("H", "h", 1)
    print('Library:', library)
    print('adding', "I")
    library.add("I", "i", 1)
    print('Library:', library)
    print('adding', "G")
    library.add("G", "g", 1)
    print('Library:', library)
    print('removing', "L")
    library.remove("L")
    print('Library:', library)
    print('removing', "H")
    library.remove("H")
    print('Library:', library)
    print('removing', "I")
    library.remove("I")
    print('Library:', library)
    print('removing', "G")
    library.remove("G")
    print('Library:', library)


before = time()
newlibrary = build_library('movies.txt')
after = time()
time_taken = round(after - before, 3)

print("Time to build: %fs" % time_taken)

before_2 = time()
movie = newlibrary.search('Iron Man')
after_2 = time()
time_taken_2 = after_2 - before_2

print("%s found in %fs" % (movie, time_taken_2))

# test()
