"""CS2515 Assignment 2 Submission.

Script Name: bst.py
Author: Conor Fox 119322236
"""


class BSTNode:
    """An internal node for a Binary Search Tree."""

    def __init__(self, item):
        """Initialise a BSTNode on creation, with value==item."""
        self._item = item
        self._left = None
        self._right = None
        self._parent = None

    def __str__(self):
        """Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        if self._left is None and self._right is None:
            return str(self._item)
        elif self._right is None and self._left is not None:
            return str(self._left) + ", " + str(self._item)
        elif self._left is None and self._right is not None:
            return str(self._item) + ", " + str(self._right)
        return str(self._left)+", "+str(self._item)+", "+str(self._right)

    def search(self, searchitem):
        """Return object matching searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST
        """
        node = self.search_node(searchitem)
        if node is not None:
            return node._item

    def search_node(self, searchitem):
        """Return the BSTNode (with subtree) containing searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST
        """
        if self._item is None:
            return None
        elif self._item == searchitem:
            pass
        elif not self._left and not self._right:
            return None
        elif searchitem < self._item:
            if not self._left:
                return None
            return self._left.search_node(searchitem)
        elif self._item < searchitem:
            if not self._right:
                return None
            return self._right.search_node(searchitem)
        return self

    def add(self, obj):
        """Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        if self._item is None:
            self._item = obj
        elif self.search(obj):
            return None
        elif obj < self._item:
            if not self._left:
                new = BSTNode(obj)
                self._left = new
                new._parent = self
            else:
                self._left.add(obj)
        elif obj > self._item:
            if not self._right:
                new = BSTNode(obj)
                self._right = new
                new._parent = self
            else:
                self._right.add(obj)
        return obj

    def findmaxnode(self):
        """Return the BSTNode with maximal element at or below here."""
        if not self._right:
            return self
        return self._right.findmaxnode()

    def height(self):
        """Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
        if not self._left and not self._right:
            return 0
        elif self._left and not self._right:
            return 1 + self._left.height()
        elif self._right and not self._left:
            return 1 + self._right.height()
        return 1 + max(self._left.height(), self._right.height())

    def size(self):
        """Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree,
        including this node.
        """
        if not self._left and not self._right:
            return 1
        elif self._left and not self._right:
            return 1 + self._left.size()
        elif self._right and not self._left:
            return 1 + self._right.size()
        return 1 + self._left.size() + self._right.size()

    def leaf(self):
        """Return True if this node has no children."""
        if not self._left and not self._right:
            return True
        return False

    def semileaf(self):
        """Return True if this node has exactly one child."""
        if self._left and not self._right:
            return True
        elif not self._left and self._right:
            return True
        return False

    def full(self):
        """Return true if this node has two children."""
        if self._left and self._right:
            return True
        return False

    def internal(self):
        """Return True if this node has at least one child."""
        if self._left or self._right:
            return True
        return False

    def remove(self, searchitem):
        """Remove and return the object matching searchitem, if there.

        Args:
            searchitem - an object of any class stored in the BST

        Remove the matching object from the tree rooted at this node.
        Maintains the BST properties.
        """
        node = self.search_node(searchitem)
        if node:
            original_item = node._item
            node.remove_node()
            return original_item

    def remove_node(self):
        """Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        original_item = self._item
        if self.full():
            big_node = self._left.findmaxnode()  # Biggest item on left
            self._item = big_node._item  # Swap current item with biggest item
            big_node.remove_node()  # Remove the previous biggest item's node
        elif self.leaf():
            parent = self._parent
            if parent is not None:  # If node has a parent,
                if parent._left is self:  # Set parent's child ref to None
                    parent._left = None
                elif parent._right is self:
                    parent._right = None
            self.clear_node()
        elif not self._right:
            leftchild = self._left
            self._item = leftchild._item  # Move item from leftchild to self
            if leftchild._left:  # Link leftchild's leftchild to self
                self._left = leftchild._left
                leftchild._left._parent = self
            else:
                self._left = None
            if leftchild._right:  # Link leftchild's rightchild to self
                self._right = leftchild._right
                leftchild._right._parent = self
            else:
                self._right = None
            leftchild.clear_node()
        else:
            rightchild = self._right
            self._item = rightchild._item
            if rightchild._left:
                rightchild._left._parent = self
                self._left = rightchild._left
            else:
                self._left = None
            if rightchild._right:
                rightchild._right._parent = self
                self._right = rightchild._right
            else:
                self._right = None
            rightchild.clear_node()
        return original_item

    def clear_node(self):
        self._item = None
        self._parent = None
        self._left = None
        self._right = None

    def _print_structure(self):
        """(Private) Print a structured representation of tree at this node."""
        if self._isthisapropertree() is False:
            print("ERROR: this is not a proper Binary Search Tree. ++++++++++")
        outstr = str(self._item) + ' (hgt=' + str(self.height()) + ')['
        if self._left is not None:
            outstr = outstr + "left: " + str(self._left._item)
        else:
            outstr = outstr + 'left: *'
        if self._right is not None:
            outstr += "; right: " + str(self._right._item) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self._parent._item)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self._left is not None:
            self._left._print_structure()
        if self._right is not None:
            self._right._print_structure()

    def _properBST(self):
        """Return True if this is the root of a proper BST; False otherwise.

        First checks that this is a proper tree (i.e. parent and child
        references all link up properly.

        Then checks that it obeys the BST property.
        """
        if not self._isthisapropertree():
            return False
        return self._BSTproperties()[0]

    def _BSTproperties(self):
        """Return a tuple describing state of this node as root of a BST.

        Returns:
            (boolean, minvalue, maxvalue):
                boolean is True if it is a BST, and false otherwise
                minvalue is the lowest value in this subtree
                maxvalue is the highest value in this subtree
        """
        minvalue = self._item
        maxvalue = self._item
        if self._left is not None:
            leftstate = self._left._BSTproperties()
            if not leftstate[0] or leftstate[2] > self._item:
                return (False, None, None)
            minvalue = leftstate[1]

        if self._right is not None:
            rightstate = self._right._BSTproperties()
            if not rightstate[0] or rightstate[1] < self._item:
                return (False, None, None)
            maxvalue = rightstate[2]

        return (True, minvalue, maxvalue)

    def _isthisapropertree(self):
        """Return True if this node is a properly implemented tree."""
        ok = True
        if self._left is not None:
            if self._left._parent != self:
                ok = False
            if self._left._isthisapropertree() is False:
                ok = False
        if self._right is not None:
            if self._right._parent != self:
                ok = False
            if self._right._isthisapropertree() is False:
                ok = False
        if self._parent is not None:
            if (self._parent._left != self
                    and self._parent._right != self):
                ok = False
        return ok
