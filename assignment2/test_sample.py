from functools import total_ordering
from bst import BSTNode


@total_ordering
class TestClass:
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


def _testadd():
    node = BSTNode(TestClass("Memento", "11/10/2000"))
    node._print_structure()
    print('> adding Melvin and Howard')
    node.add(TestClass("Melvin and Howard", "19/09/1980"))
    node._print_structure()
    print('> adding a second version of Melvin and Howard')
    node.add(TestClass("Melvin and Howard", "21/03/2007"))
    node._print_structure()
    print('> adding Mellow Mud')
    node.add(TestClass("Mellow Mud", "21/09/2016"))
    node._print_structure()
    print('> adding Melody')
    node.add(TestClass("Melody", "21/03/2007"))
    node._print_structure()
    return node


def _test():
    node = BSTNode(TestClass("B", "b"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "A")
    node.add(TestClass("A", "a"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "A")
    node.remove(TestClass("A"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "C")
    node.add(TestClass("C", "c"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "C")
    node.remove(TestClass("C"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "F")
    node.add(TestClass("F", "f"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "B")
    node.remove(TestClass("B"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "C")
    node.add(TestClass("C", "c"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "D")
    node.add(TestClass("D", "d"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "C")
    node.add(TestClass("C", "c"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "E")
    node.add(TestClass("E", "e"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "B")
    node.remove(TestClass("B"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "D")
    node.remove(TestClass("D"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "C")
    node.remove(TestClass("C"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "E")
    node.remove(TestClass("E"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "L")
    node.add(TestClass("L", "l"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "H")
    node.add(TestClass("H", "h"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "I")
    node.add(TestClass("I", "i"))
    print('Ordered:', node)
    node._print_structure()
    print('adding', "G")
    node.add(TestClass("G", "g"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "L")
    node.remove(TestClass("L"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "H")
    node.remove(TestClass("H"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "I")
    node.remove(TestClass("I"))
    print('Ordered:', node)
    node._print_structure()
    print('removing', "G")
    node.remove(TestClass("G"))
    print('Ordered:', node)
    node._print_structure()
    print(node)


BSTNode._testadd()
print('++++++++++')
BSTNode._test()
