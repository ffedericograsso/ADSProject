#TreeNode rappresenta un nodo generico dell'albero, con chiave, puntatori a sinistra e destra, e un puntatore al genitore.
class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self

#BST implementa un albero binario di ricerca con operazioni di inserimento, rimozione, rotazione e ricerca. La classe AVL estende BST aggiungendo il bilanciamento automatico dopo ogni inserimento o rimozione, garantendo che l'albero rimanga bilanciato.
#Guardare AVL per vedere i commenti sulle funzioni di bilanciamento e gestione dell'altezza.
class BST:
    
    def __init__(self, root = None):
        self.root = root
    
    def __str__(self):
        if self.root == None:
            return "NULL "
        else:
            return f"{self.root.key} " + BST(self.root.left).__str__() + BST(self.root.right).__str__()

    def find(self, key):
        if self.root is None:
            return None
        if self.root.key == key:
            return self.root
        elif key < self.root.key:
            return BST(self.root.left).find(key)
        else:
            return BST(self.root.right).find(key)
        

    def nxt(self, node):
        if node is None:
            return None
        
        if node.right is not None:
            return self.min(node.right)
        else:
            parent = node.parent
            while parent is not None and node == parent.right:
                node = parent
                parent = parent.parent
            return parent

    def min(self, node):
        while node.left is not None:
            node = node.left
        return node
    

    def prv(self, node):
        if node is None:
            return None
        
        if node.left is not None:
            return self.max(node.left)
        else:
            parent = node.parent
            while parent is not None and node == parent.left:
                node = parent
                parent = parent.parent
            return parent

    def max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def insert(self, node):
        y = None
        x = self.root
        while x is not None: 
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node 
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def remove(self, node):
        if node.left is not None and node.right is not None:
            successor = self.nxt(node)
            node.key = successor.key
            self.remove(successor)
        elif node.left is not None:
            if node.parent is None:
                self.root = node.left
                node.left.parent = None
            elif node == node.parent.left:
                node.parent.left = node.left
                node.left.parent = node.parent
            else:
                node.parent.right = node.left
                node.left.parent = node.parent
        elif node.right is not None:
            if node.parent is None:
                self.root = node.right
                node.right.parent = None
            elif node == node.parent.left:
                node.parent.left = node.right
                node.right.parent = node.parent
            else:
                node.parent.right = node.right
                node.right.parent = node.parent
        else:
            if node.parent is None:
                self.root = None
            elif node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

    def rotate_right(self, node):
        if node.left is None:
            return
        left = node.left
        node.left = left.right
        if left.right is not None:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.left:
            node.parent.left = left
        else:
            node.parent.right = left
        left.right = node
        node.parent = left

    def rotate_left(self, node):
        if node.right is None:
            return
        right = node.right
        node.right = right.left
        if right.left is not None:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right
