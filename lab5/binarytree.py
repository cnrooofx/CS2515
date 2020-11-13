"""Binary Tree implementation."""


class BTNode:
    """Node to be used in a Binary Tree."""

    def __init__(self, element, parent=None, leftchild=None, rightchild=None):
        """Create a BTNode."""
        self.element = element
        self.parent = parent
        self.left = leftchild
        self.right = rightchild

    def getElement(self):
        """Return the element in the node."""
        return self.element

    def setElement(self, element):
        """Change the element in the node."""
        self.element = element

    def getParent(self):
        """Return the parent of the node."""
        return self.parent

    def setParent(self, parent):
        """Change the parent of the node."""
        self.parent = parent

    def getLeftChild(self):
        """Return the Left Child of the node."""
        return self.left

    def setLeftChild(self, leftchild):
        """Change the Left Child of the node."""
        self.left = leftchild

    def getRightChild(self):
        """Return the Right Child of the node."""
        return self.left
        return self.right

    def setRightChild(self, rightchild):
        """Change the Right Child of the node."""
        self.right = rightchild

    def removeLeft(self):
        """Remove and return the Left subtree."""
        if self.left is None:
            return None
        self.left.parent = None
        left_tree = self.left
        self.left = None
        return left_tree

    def removeRight(self):
        """Remove and return the Right subtree."""
        if self.right is None:
            return None
        self.right.parent = None
        right_tree = self.right
        self.right = None
        return right_tree

    def __str__(self):
        """Return a string representation of the Node."""
        if self.parent is None:
            parent = "*"
        else:
            parent = str(self.parent.element)
        if self.left is None:
            left = "*"
        else:
            left = str(self.left.element)
        if self.right is None:
            right = "*"
        else:
            right = str(self.right.element)
        return "{}, [{}, {}] -- {}".format(self.element, left, right, parent)


def main():
    """Test methods for Binary Tree class."""
    print("Binary Tree Node")
    node = BTNode("A")
    print(node.getElement())
    node.setElement("AA")
    node2 = BTNode("B")
    node3 = BTNode("C")
    node2.setParent(node)
    print(node2.getParent())
    node.setLeftChild(node2)
    node3.setParent(node2)
    node2.setRightChild(node3)
    print(node)
    print(node2)
    print(node.removeLeft())
    print(node)


if __name__ == '__main__':
    main()
