"""Binary Tree implementation."""


class BTNode:
    """Node to be used in a Binary Tree."""

    def __init__(self, element, parent=None, leftchild=None, rightchild=None):
        """Create a BTNode."""
        self.element = element
        self.parent = parent
        self.left = leftchild
        self.right = rightchild

    def get_element(self):
        """Return the element in the node."""
        return self.element

    def set_element(self, element):
        """Change the element in the node."""
        self.element = element

    def get_parent(self):
        """Return the parent of the node."""
        return self.parent

    def set_parent(self, parent):
        """Change the parent of the node."""
        self.parent = parent

    def get_left_child(self):
        """Return the Left Child of the node."""
        return self.left

    def set_left_child(self, leftchild):
        """Change the Left Child of the node."""
        self.left = leftchild
        leftchild.parent = self

    def get_right_child(self):
        """Return the Right Child of the node."""
        return self.right

    def set_right_child(self, rightchild):
        """Change the Right Child of the node."""
        self.right = rightchild
        rightchild.parent = self

    def remove_left(self):
        """Remove and return the Left subtree."""
        if self.left is None:
            return None
        self.left.parent = None
        left_tree = self.left
        self.left = None
        return left_tree

    def remove_right(self):
        """Remove and return the Right subtree."""
        if self.right is None:
            return None
        self.right.parent = None
        right_tree = self.right
        self.right = None
        return right_tree

    def inorder(self):
        if self.left is None:
            return self.element
        elif self.right is None:
            return self.element
        return self.left.inorder() + self.element + self.right.inorder()

    def height(self):
        if self.right is None and self.left is None:
            return 1
        return max(self.left.height(), self.right.height()) + 1

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


def inorder_traversal(node):
    if node.left is not None:
        inorder_traversal(node.left)
    print(node.element)
    if node.right is not None:
        inorder_traversal(node.right)


def main():
    """Test methods for Binary Tree class."""
    print("Binary Tree Node")
    node = BTNode("A")
    print(node.get_element())
    node.set_element("AA")
    node2 = BTNode("B")
    node3 = BTNode("C")
    node2.set_parent(node)
    print(node2.get_parent())
    node.set_left_child(node2)
    node3.set_parent(node2)
    node2.set_right_child(node3)
    print(node)
    print(node2)
    print(node.remove_left())
    print(node)

    print("\nInorder Traversal")
    node0 = BTNode("C")
    node1 = BTNode("o")
    node2 = BTNode("n")
    node3 = BTNode("O")
    node4 = BTNode("r")
    node3.set_left_child(node1)
    node3.set_right_child(node4)
    node1.set_left_child(node0)
    node1.set_right_child(node2)

    num1 = BTNode(1)
    num2 = BTNode(2)
    num3 = BTNode(3)
    num4 = BTNode(4)
    num5 = BTNode(5)
    num6 = BTNode(6)
    num7 = BTNode(7)
    num8 = BTNode(8)
    num9 = BTNode(9)
    num6.set_left_child(num2)
    num6.set_right_child(num8)
    num2.set_left_child(num1)
    num2.set_right_child(num4)
    num4.set_left_child(num3)
    num4.set_right_child(num5)
    num8.set_left_child(num7)
    num8.set_right_child(num9)

    print("v0")
    # inorder_traversal(node3)
    # inorder_traversal(num6)
    print(node3.inorder())
    print(node3.height())


if __name__ == "__main__":
    main()
