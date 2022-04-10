from typing import Tuple
from node import *


class BinarySearchTree:
    _size = 0
    _root = None

    def __init__(self):
        pass

    def _get_root(self):
        """Get the root Node"""

        return self._root

    def _sub_size(self, root: Node):
        """Get teh size of a tree or sub-tree using recursion"""

        if root is None:
            return 0
        else:
            return self._sub_size(root.left) + 1 + self._sub_size(root.right)

    def _add(self, root: Node, key: int, value: str):
        """Insert node to BST"""

        if root:
            if key == root.key:
                return root

            elif key < root.key:
                if root.left is None:
                    root.left = Node(key, value, parent=root)
                    self._size += 1
                else:
                    self._add(root.left, key, value)

            else:
                if root.right is None:
                    root.right = Node(key, value, parent=root)
                    self._size += 1
                else:
                    self._add(root.right, key, value)

        elif self._get_root() is None:
            self._root = Node(key, value)
            self._size += 1

    def _search(self, root: Node, key: int):
        """Search and return node in the BST"""

        if root:
            if root.key == key:
                return root
            elif key <= root.key:
                return self._search(root.left, key)
            else:
                return self._search(root.right, key)
        else:
            return None

    def _preorder_walk(
        self, root: Node = None, meet: list = None, size: int = None
    ) -> list:
        """Traverse the tree in preorder and return traversed nodes in preorder"""

        if meet is None:  # for storing traversed nodes in given order
            meet = []
            size = self.size() if root == self._get_root() else self._sub_size(root)

        if not root:  # remove recursion from call stack when None
            return

        meet.append(root)  # processing node
        self._preorder_walk(root.left, meet, size)  # travesring left
        self._preorder_walk(root.right, meet, size)  # traversing right

        if len(meet) == size:  # exit and return traversed nodes when all traversed
            return meet

        return  # remove recursion from call stack when done traversing node

    def _inorder_walk(
        self, root: Node = None, meet: list = None, size: int = None
    ) -> list:
        """Traverse the tree in preorder and return traversed nodes in inorder"""

        if meet is None:  # for storing traversed nodes in given order
            meet = []
            size = self.size() if root == self._get_root() else self._sub_size(root)

        if not root:  # remove recursion from call stack when None
            return

        self._inorder_walk(root.left, meet, size)  # traverse left
        meet.append(root)  # processing node
        self._inorder_walk(root.right, meet, size)  # traverse right

        if len(meet) == size:  # return traversed nodes when traversing complete
            return meet

        return  # remove recursion from call stack when done traversing node

    def _postorder_walk(
        self, root: Node = None, meet: list = None, size: int = None
    ) -> list:
        """Traverse the tree in preorder and return traversed nodes in postorder"""

        if meet is None:  # for storing traversed nodes in given order
            meet = []
            size = self.size() if root == self._get_root() else self._sub_size(root)

        if not root:  # remove recursion from call stack when None
            return

        self._postorder_walk(root.left, meet, size)  # traverse left
        self._postorder_walk(root.right, meet, size)  # traverse right
        meet.append(root)  # process node

        if len(meet) == size:  # return traversed nodes when traversing complete
            return meet

        return  # remove recursion from call stack when done traversing node

    def _smallest(self, root=None):
        smallest = root

        while smallest.right is not None:  # iteratively traverse left until no elements
            smallest = smallest.left

        return smallest  # return smallest leaf

    def _largest(self, root=None):
        largest = root

        while largest.right is not None:  # iteratively traverse right until no elements
            largest = largest.right

        return largest  # return largest leaf

    def _remove(self, root: Node, key: int):

        if root:
            if root.key == key:

                ##
                # CASE FOR NO CHILDREN
                if root.left is None and root.right is None:
                    node_to_delete = root
                    node_to_delete_parent = root.parent

                    ## checking if node-to-delete is root
                    # if not, removing node-to-delete references from it's parent
                    if node_to_delete_parent:  # if the node-to-delete has parent
                        if node_to_delete is node_to_delete_parent.left:
                            node_to_delete_parent.left = None
                        else:
                            node_to_delete_parent.right = None

                    del root
                    self._size -= 1

                ##
                # CASE FOR SINGLE CHILD
                elif root.left is None or root.right is None:

                    node_to_delete = root
                    node_to_delete_left_child = root.left  # might not exist
                    node_to_delete_right_child = root.right  # might not exist
                    node_to_delete_parent = root.parent  # doesn't exist for tree root

                    ## change in replacement's attributes
                    # making replacement node-to-delete's left/right child
                    if node_to_delete_left_child:
                        replacement_single_child = node_to_delete_left_child
                    else:
                        replacement_single_child = node_to_delete_right_child

                    ## change in deleted node's parents
                    # if not root, making replacement child's parent node-to-delete's parent
                    #       making replacement child the node-to-delete's parents left/right child
                    if node_to_delete_parent:  # if node-to-delete has parents
                        replacement_single_child.parent = node_to_delete_parent

                        # checking whether node-to-delete was the right or left child
                        if node_to_delete_parent.left == node_to_delete:
                            node_to_delete_parent.left = replacement_single_child
                        else:
                            node_to_delete_parent.right = replacement_single_child

                    del root
                    del replacement_single_child
                    self._size -= 1

                ##
                # CASE FOR DOUBLE CHILDREN
                elif root.left is not None and root.right is not None:
                    inorder_predecessor = self._inorder_walk(root.left)[
                        -1
                    ]  # inorder predecessor must exist as node-to-delete has two children

                    node_to_delete_parent = root.parent  # might not exist for tree root
                    node_to_delete_left_child = root.left  # exists as two children
                    node_to_delete_right_child = root.right  # exists as two children

                    ## change in node-to-delete's children attributes
                    # since the node-to-delete is deleted, removing its
                    # references from its children
                    node_to_delete_right_child.parent = inorder_predecessor

                    ## change inorder predecessors parent attributes
                    # since removing predecessor, removing predecessor
                    # references from predecessor's parent
                    if inorder_predecessor.parent.left is inorder_predecessor:
                        inorder_predecessor.parent.left = None
                    elif inorder_predecessor.parent.right is inorder_predecessor:
                        inorder_predecessor.parent.right = None

                    ## change in inorder predecessor attributes
                    # since predecessor is being replaced in new place
                    # adding previous node-to-delete's children, parent to predecessor
                    inorder_predecessor.left = (
                        node_to_delete_left_child
                        if inorder_predecessor is not node_to_delete_left_child
                        else None
                    )
                    # ^- since replacing with inorder predecessor, checking node-to-delete's left is
                    # predecessor itself to avoid self reference
                    inorder_predecessor.right = node_to_delete_right_child

                    ## checking node-to-delete is root if not changing accordingly
                    # if root, making predecessor root
                    # if not root, making predecessor node-to-delete's parents's left child
                    #       and node-to-delete's parent predecessor's parent
                    if node_to_delete_parent:
                        node_to_delete_parent.left = inorder_predecessor
                        inorder_predecessor.parent = node_to_delete_parent
                    else:
                        root = inorder_predecessor
                        self._root = inorder_predecessor

                    # delete from memory
                    del root
                    del inorder_predecessor
                    self._size -= 1

            elif key < root.key:
                return self._remove(root.left, key)

            else:
                return self._remove(root.right, key)
        else:
            return None

    ##################################
    # PUBLIC METHODS
    ##################################

    def size(self):
        """Return size of the bst"""

        return self._size

    def recursive_size(self):
        """Return size of tree by recursive calculation"""

        return self._sub_size(self._get_root())

    def add(self, key: int, value: str):
        """Insert key value into BST"""

        self._add(self._get_root(), key, value)

    def search(self, key: int):
        """Search in BST using key"""

        found_node = self._search(self._get_root(), key)
        return found_node.value if found_node else None

    def preorder_walk(self):
        """Return list of keys for pre-orderly traversed BST"""

        meetup = self._preorder_walk(self._get_root())
        return [node.key for node in meetup]

    def inorder_walk(self):
        """Return list of keys for in-orderly traversed BST"""

        meetup = self._inorder_walk(self._get_root())
        return [node.key for node in meetup]

    def postorder_walk(self):
        """Return list of key for post-orderly traversed BST"""

        meetup = self._postorder_walk(self._get_root())
        return [node.key for node in meetup]

    def smallest(self) -> tuple():
        """Return tuple containing key and value of smallest node"""

        smallest_node = self._smallest(self._get_root())
        return (smallest_node.key, smallest_node.value)

    def largest(self):
        """Return tuple containing key and value of largest node"""

        largest_node = self._largest(self._get_root())
        return (largest_node.key, largest_node.value)

    def remove(self, key: int):
        """Remove node from BST using key"""

        self._remove(self._get_root(), key)
