class Node:
    key = None
    value = None
    left = None
    right = None
    parent = None

    def __init__(self, key, value, left=None, right=None, parent=None):

        assert key != None
        assert value != None

        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
