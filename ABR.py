class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def get(self):
        return self.key

    def set(self, newkey):
        self.key = newkey

    def getChildren(self):
        children = []
        if self.left != None:
            children.append(self.left)
        if self.right != None:
            children.append(self.right)
        return children

class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, node):
        self.root = node

    def insert(self, key):
        if self.root is None:
            self.setRoot(Node(key))
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if key <= currentNode.get():
            if currentNode.left:
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
        else:
            if currentNode.right:
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if currentNode is None:
            return False
        elif currentNode.get() == key:
            return True
        elif currentNode.get() > key:
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def inorder(self):
        print("start tree")
        self._inorder(self.root)
        print("end tree")

    def _inorder(self, v):
        if v is None:
            return
        self._inorder(v.left)
        print(v.get())
        self._inorder(v.right)

