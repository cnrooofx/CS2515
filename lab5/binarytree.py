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


def main():
    """Test methods for Binary Tree class."""
    print("Binary Tree Node")
    node = BTNode("A")
    print(node.getElement())
    node.setElement("AA")
    node2 = BTNode("B")
    node.setParent(node2)
    print(node.getParent())


if __name__ == '__main__':
    main()
