from ABR import Node
from ABR import ABR

class RNode(Node):
    def __init__(self, key, color):
        self.color = color                   #nero = true, rosso = false
        self.p = None                        #p puntatore al padre, indispesabile per un albero RN
        Node.__init__(self, key)

    def getColor(self):
        return self.color

    def setColor(self, newcolor):
        self.color = newcolor

    def getP(self):
        return self.p

    def setP(self, newP):
        self.p = newP

class RN(ABR):
    def __init__(self):
        ABR.__init__(self)
        self.nil = RNode(None, True)               #nil è un nodo senza key, ma nero

    def setRoot(self, node):
        ABR.setRoot(self, node)
        self.root.setP(self.nil)   #viene impostato il padre della radice a nil

    def insert(self, key):
        if self.root is None:
            self.setRoot(RNode(key, True))
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):        #questo inserimento non prevede l'inizializzazione col primo nodo
        newP = None
        while currentNode is not None:           #pertanto almeno un ciclo viene eseguito
            if key <= currentNode.get():
                newP = currentNode
                currentNode = currentNode.left
            else:
                newP = currentNode
                currentNode = currentNode.right
        currentNode = RNode(key, False)
        currentNode.setP(newP)
        if key <= newP.get():                    #dunque non vi è la possibilità che currentNode sia la radice
            newP.left = currentNode
        else:
            newP.right = currentNode
        self.insertFixUp(currentNode)

    def insertFixUp(self, z):
        while not z.getP().getColor():
            if z.getP() == z.getP().getP().left:
                y = z.getP().getP().right
                if y is not None and not y.getColor():
                    y.setColor(True)
                    z.getP().setColor(True)
                    z.getP().getP().setColor(False)
                    z = z.getP().getP()
                else:
                    if z.getP().right == z:
                        z = z.getP()
                        self.leftRotate(z)
                    z.getP().setColor(True)
                    z.getP().getP().setColor(False)
                    self.rightRotate(z.getP().getP())
            else:
                y = z.getP().getP().left
                if y is not None and not y.getColor():
                    y.setColor(True)
                    z.getP().setColor(True)
                    z.getP().getP().setColor(False)
                    z = z.getP().getP()
                else:
                    if z.getP().left == z:
                        z = z.getP()
                        self.rightRotate(z)
                    z.getP().setColor(True)
                    z.getP().getP().setColor(False)
                    self.leftRotate(z.getP().getP())
        self.root.setColor(True)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.setP(x)
        y.setP(x.getP())
        if x == self.root:
            self.setRoot(y)
        elif x == x.getP().left:
            x.getP().left = y
        else:
            x.getP().right = y
        y.left = x
        x.setP(y)

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.setP(x)
        y.setP(x.getP())
        if x == self.root:
            self.setRoot(y)
        elif x == x.getP().left:
            x.getP().left = y
        else:
            x.getP().right = y
        y.right = x
        x.setP(y)