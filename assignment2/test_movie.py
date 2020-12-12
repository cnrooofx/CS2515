from bst import BSTNode
from movieLib import MovieLib
from functools import total_ordering


@total_ordering
class STestClass:
    """ Represents an arbitrary thing, for testing the BST. """

    def __init__(self, field1, field2=None):
        """ Initialise an object. """
        self._field1 = field1
        self._field2 = field2

    def __str__(self):
        """ Return a short string representation of this object. """
        outstr = self._field1
        return outstr

    def full_str(self):
        """ Return a full string representation of this object. """
        outstr = self._field1 + ": "
        outstr = outstr + str(self._field2)
        return outstr

    def __eq__(self, other):
        """ Return True if this object has exactly same field1 as other. """
        if (other._field1 == self._field1):
            return True
        return False

    def __ne__(self, other):
        """ Return False if this object has exactly same field1 as other. """
        return not (self._field1 == other._field1)

    def __lt__(self, other):
        """ Return True if this object is ordered before other.

        A thing is less than another if it's field1 is alphabetically before.
        """
        if other._field1 > self._field1:
            return True
        return False


class TestBTN:
    def test_add(self, capsys):
        node = BSTNode(STestClass("Memento", "11/10/2000"))
        assert node._element == STestClass("Memento", "11/10/2000")
        node.add(STestClass("Melvin and Howard", "19/09/1980"))
        node.add(STestClass("Melvin and Howard", "21/03/2007"))
        node.add(STestClass("Mellow Mud", "21/09/2016"))
        node.add(STestClass("Melody", "21/03/2007"))

    def test_string(self, capsys):
        node = BSTNode(STestClass("Memento", "11/10/2000"))
        node.add(STestClass("Melvin and Howard", "19/09/1980"))
        node.add(STestClass("Mellow Mud", "21/09/2016"))
        node.add(STestClass("Melody", "21/03/2007"))
        print(node)
        capt = capsys.readouterr()
        assert capt.out == "Mellow Mud, Melody, Melvin and Howard, Memento\n"

    def test_search_node(self):
        node = BSTNode(STestClass("A", "a"))
        node.add(STestClass("G", "g"))
        node.add(STestClass("H", "h"))
        node.add(STestClass("B", "b"))
        node.add(STestClass("Z", "z"))

        search_node = node.search_node(STestClass("G", "g"))
        assert search_node._element.full_str() == "G: g"

    def test_search(self):
        node = BSTNode(STestClass("A", "a"))
        node.add(STestClass("G", "g"))
        node.add(STestClass("H", "h"))
        node.add(STestClass("B", "b"))
        node.add(STestClass("Z", "z"))

        search_item = node.search_node(STestClass("C", "c"))
        assert search_item is None

        search_item = node.search(STestClass("H", "h"))
        assert search_item.full_str() == "H: h"

    def test_findmaxnode(self):
        node = BSTNode("a")
        node.add("b")
        node.add("c")
        assert str(node.findmaxnode()) == "c"

        node = BSTNode("e")
        node.add("g")
        node.add("o")
        node.add("h")
        node.add("k")
        node.add("m")
        node.add("l")
        assert str(node.findmaxnode()) == "o"

    def test_height(self):
        pass

    def test_size(self):
        node = BSTNode("e")
        assert node.size() == 1

        node.add("g")
        node.add("o")
        node.add("h")
        node.add("k")
        node.add("m")
        node.add("l")
        assert node.size() == 7

    def test_add_remove(self):
        node = BSTNode(STestClass("B", "b"))
        out = str(node)
        assert out == "B"

        node.add(STestClass("A", "a"))
        out = str(node)
        assert out == "A, B"

        node.remove(STestClass("A"))
        out = str(node)
        assert out == "B"

        node.add(STestClass("C", "c"))
        out = str(node)
        assert out == "B, C"

        node.remove(STestClass("C"))
        out = str(node)
        assert out == "B"

        node.add(STestClass("F", "f"))
        out = str(node)
        assert out == "B, F"

        node.remove(STestClass("B"))
        out = str(node)
        assert out == "F"

        node.add(STestClass("C", "c"))
        out = str(node)
        assert out == "C, F"

        node.add(STestClass("D", "d"))
        out = str(node)
        assert out == "C, D, F"

        node.add(STestClass("C", "c"))
        out = str(node)
        assert out == "C, D, F"

        node.add(STestClass("E", "e"))
        out = str(node)
        assert out == "C, D, E, F"

        node.remove(STestClass("B"))
        out = str(node)
        assert out == "C, D, E, F"

        node.remove(STestClass("D"))
        out = str(node)
        assert out == "C, E, F"

        node.remove(STestClass("C"))
        out = str(node)
        assert out == "E, F"

        node.remove(STestClass("E"))
        out = str(node)
        assert out == "F"

        node.add(STestClass("L", "l"))
        out = str(node)
        assert out == "F, L"

        node.add(STestClass("H", "h"))
        out = str(node)
        assert out == "F, H, L"

        node.add(STestClass("I", "i"))
        out = str(node)
        assert out == "F, H, I, L"

        node.add(STestClass("G", "g"))
        out = str(node)
        assert out == "F, G, H, I, L"

        node.remove(STestClass("L"))
        out = str(node)
        assert out == "F, G, H, I"

        node.remove(STestClass("H"))
        out = str(node)
        assert out == "F, G, I"

        node.remove(STestClass("I"))
        out = str(node)
        assert out == "F, G"

        node.remove(STestClass("G"))
        out = str(node)
        assert out == "F"

        assert node._properBST()


class TestLibrary:
    def test_add(self):
        library = MovieLib()

        add = library.add("Wonder Bar", "31/03/1934", "84")
        assert str(add) == "Wonder Bar"
        assert library.bst._properBST()

        add = library.add("Wonder Man", "01/01/1945", "98")
        assert str(add) == "Wonder Man"
        assert library.bst._properBST()

        add = library.add("Wonderwall", "17/05/1968", "92")
        assert str(add) == "Wonderwall"
        assert library.bst._properBST()

        add = library.add("Wonder Women", "25/04/1973", "82")
        assert str(add) == "Wonder Women"
        assert library.bst._properBST()

        add = library.add("Wonder Woman", "12/03/1974", "75")
        assert str(add) == "Wonder Woman"
        assert library.bst._properBST()

        add = library.add("Won Ton Ton: the Dog Who Saved Hollywood", "26/07/1976", "92")
        assert str(add) == "Won Ton Ton: the Dog Who Saved Hollywood"
        assert library.bst._properBST()

        add = library.add("Women's Prison Massacre", "31/08/1983", "89")
        assert str(add) == "Women's Prison Massacre"
        assert library.bst._properBST()

        add = library.add("Wonderland", "17/10/1997", "0")
        assert str(add) == "Wonderland"
        assert library.bst._properBST()

        add = library.add("Wonderland", "13/05/1999", "108")
        assert add is None

        add = library.add("Wonder Boys", "22/02/2000", "111")
        assert str(add) == "Wonder Boys"
        assert library.bst._properBST()

        add = library.add("Women's Prison", "06/10/2002", "106")
        assert str(add) == "Women's Prison"
        assert library.bst._properBST()

        add = library.add("Wonderful Days", "17/07/2003", "86")
        assert str(add) == "Wonderful Days"
        assert library.bst._properBST()

        add = library.add("Wonderland", "06/10/2002", "106")
        assert add is None

        add = library.add("Wonderful and Loved by All", "24/08/2007", "106")
        assert str(add) == "Wonderful and Loved by All"
        assert library.bst._properBST()

        add = library.add("Wonderful World", "01/01/2009", "89")
        assert str(add) == "Wonderful World"
        assert library.bst._properBST()

        add = library.add("Wonder Woman", "03/03/2009", "74")
        assert add is None

        add = library.add("Women Without Men", "11/09/2009", "100")
        assert str(add) == "Women Without Men"
        assert library.bst._properBST()

        add = library.add("Women Vs Men", "04/02/2011", "98")
        assert str(add) == "Women Vs Men"
        assert library.bst._properBST()

        add = library.add("Wonder Women!: The Untold Story of American Superheroines", "10/03/2012", "55")
        assert str(add) == "Wonder Women!: The Untold Story of American Superheroines"
        assert library.bst._properBST()

        add = library.add("Women's Day", "08/05/2012", "90")
        assert str(add) == "Women's Day"
        assert library.bst._properBST()

        add = library.add("Women Who Flirt", "28/11/2014", "97")
        assert str(add) == "Women Who Flirt"
        assert library.bst._properBST()

        add = library.add("Women vs. Men", "01/04/2015", "90")
        assert str(add) == "Women vs. Men"
        assert library.bst._properBST()

        add = library.add("Wonder Woman", "30/05/2017", "141")
        assert add is None

    def test_size(self):
        library = MovieLib()
        filecount = 0

        assert library.size() == 0, "should be 0 when no tree exists"

        library.add("Wonder Bar", "31/03/1934", "84")
        filecount += 1
        library.add("Wonder Man", "01/01/1945", "98")
        filecount += 1
        library.add("Wonderwall", "17/05/1968", "92")
        filecount += 1
        library.add("Wonder Women", "25/04/1973", "82")
        filecount += 1
        library.add("Wonder Woman", "12/03/1974", "75")
        filecount += 1
        library.add("Won Ton Ton: the Dog Who Saved Hollywood", "26/07/1976", "92")
        filecount += 1
        library.add("Women's Prison Massacre", "31/08/1983", "89")
        filecount += 1
        library.add("Wonderland", "17/10/1997", "0")
        filecount += 1
        library.add("Wonder Boys", "22/02/2000", "111")
        filecount += 1
        library.add("Women's Prison", "06/10/2002", "106")
        filecount += 1
        library.add("Wonderful Days", "17/07/2003", "86")
        filecount += 1
        library.add("Wonderful and Loved by All", "24/08/2007", "106")
        filecount += 1
        library.add("Wonderful World", "01/01/2009", "89")
        filecount += 1
        library.add("Women Without Men", "11/09/2009", "100")
        filecount += 1
        library.add("Women Vs Men", "04/02/2011", "98")
        filecount += 1
        library.add("Wonder Women!: The Untold Story of American Superheroines", "10/03/2012", "55")
        filecount += 1
        library.add("Women's Day", "08/05/2012", "90")
        filecount += 1
        library.add("Women Who Flirt", "28/11/2014", "97")
        filecount += 1
        library.add("Women vs. Men", "01/04/2015", "90")
        filecount += 1

        assert filecount == library.size()

    def test_string(self, capsys):
        library = MovieLib()

        library.add("Wonder Bar", "31/03/1934", "84")
        library.add("Wonder Man", "01/01/1945", "98")
        library.add("Wonderwall", "17/05/1968", "92")
        library.add("Wonder Women", "25/04/1973", "82")
        library.add("Wonder Woman", "12/03/1974", "75")
        library.add("Won Ton Ton: the Dog Who Saved Hollywood", "26/07/1976", "92")
        library.add("Women's Prison Massacre", "31/08/1983", "89")
        library.add("Wonderland", "17/10/1997", "0")
        library.add("Wonder Boys", "22/02/2000", "111")
        library.add("Women's Prison", "06/10/2002", "106")
        library.add("Wonderful Days", "17/07/2003", "86")
        library.add("Wonderful and Loved by All", "24/08/2007", "106")
        library.add("Wonderful World", "01/01/2009", "89")
        library.add("Women Without Men", "11/09/2009", "100")
        library.add("Women Vs Men", "04/02/2011", "98")
        library.add("Wonder Women!: The Untold Story of American Superheroines", "10/03/2012", "55")
        library.add("Women's Day", "08/05/2012", "90")
        library.add("Women Who Flirt", "28/11/2014", "97")
        library.add("Women vs. Men", "01/04/2015", "90")

        print(library)
        captured = capsys.readouterr()
        assert captured.out == """Women Vs Men, Women Who Flirt, \
Women Without Men, Women vs. Men, Women's Day, Women's Prison, \
Women's Prison Massacre, Won Ton Ton: the Dog Who Saved Hollywood, \
Wonder Bar, Wonder Boys, Wonder Man, Wonder Woman, \
Wonder Women, \
Wonder Women!: The Untold Story of American Superheroines, \
Wonderful Days, Wonderful World, Wonderful and Loved by All, \
Wonderland, Wonderwall\n"""

    def test_search(self):
        library = MovieLib()

        movie = library.search("Wonder Woman")
        assert movie is None, "shouldn't search when no tree exists"

        library.add("Wonder Bar", "31/03/1934", "84")
        library.add("Wonder Man", "01/01/1945", "98")
        library.add("Wonderwall", "17/05/1968", "92")
        library.add("Wonder Women", "25/04/1973", "82")
        library.add("Wonder Woman", "12/03/1974", "75")
        library.add("Won Ton Ton: the Dog Who Saved Hollywood", "26/07/1976", "92")
        library.add("Women's Prison Massacre", "31/08/1983", "89")
        library.add("Wonderland", "17/10/1997", "0")
        library.add("Wonder Boys", "22/02/2000", "111")
        library.add("Women's Prison", "06/10/2002", "106")
        library.add("Wonderful Days", "17/07/2003", "86")
        library.add("Wonderful and Loved by All", "24/08/2007", "106")
        library.add("Wonderful World", "01/01/2009", "89")
        library.add("Women Without Men", "11/09/2009", "100")
        library.add("Women Vs Men", "04/02/2011", "98")
        library.add("Wonder Women!: The Untold Story of American Superheroines", "10/03/2012", "55")
        library.add("Women's Day", "08/05/2012", "90")
        library.add("Women Who Flirt", "28/11/2014", "97")
        library.add("Women vs. Men", "01/04/2015", "90")

        movie = library.search("Wonder Woman")
        assert str(movie) == "Wonder Woman"

        movie = library.search("Touch of Evil")
        assert movie is None

        movie = library.search("Delicatessen")
        assert movie is None

        movie = library.search("Wonder Women")
        assert str(movie) == "Wonder Women"

    def test_remove(self):
        library = MovieLib()

        remove = library.remove("Wonder Women")
        assert remove is None, "shouldn't remove when no tree exists"

        library.add("Wonder Bar", "31/03/1934", "84")
        library.add("Wonder Man", "01/01/1945", "98")
        library.add("Wonderwall", "17/05/1968", "92")
        library.add("Wonder Women", "25/04/1973", "82")
        library.add("Wonder Woman", "12/03/1974", "75")
        library.add("Won Ton Ton: the Dog Who Saved Hollywood", "26/07/1976", "92")
        library.add("Women's Prison Massacre", "31/08/1983", "89")
        library.add("Wonderland", "17/10/1997", "0")
        library.add("Wonder Boys", "22/02/2000", "111")
        library.add("Women's Prison", "06/10/2002", "106")
        library.add("Wonderful Days", "17/07/2003", "86")
        library.add("Wonderful and Loved by All", "24/08/2007", "106")
        library.add("Wonderful World", "01/01/2009", "89")
        library.add("Women Without Men", "11/09/2009", "100")
        library.add("Women Vs Men", "04/02/2011", "98")
        library.add("Wonder Women!: The Untold Story of American Superheroines", "10/03/2012", "55")
        library.add("Women's Day", "08/05/2012", "90")
        library.add("Women Who Flirt", "28/11/2014", "97")
        library.add("Women vs. Men", "01/04/2015", "90")

        remove = library.remove("Wonder Women")
        assert str(remove) == "Wonder Women"

        remove = library.remove("Iron Man")
        assert remove is None

        remove = library.remove("Wonder Women")
        assert remove is None

        remove = library.search("Women's Day")
        assert str(remove) == "Women's Day"
