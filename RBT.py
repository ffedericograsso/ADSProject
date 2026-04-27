#color restituisce il colore di un nodo, restituendo "black" se il nodo è None o se non ha un attributo "color". Altrimenti, restituisce il valore dell'attributo "color" del nodo.
def color(node):
    return getattr(node, "color", "black") if node != None else "black"

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

#guardare AVL per vedere i commenti sulle funzioni di bilanciamento e gestione dell'altezza.
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

#RBTree estende BST implementando un albero rosso-nero, che mantiene le proprietà di bilanciamento attraverso l'uso di colori (rosso e nero) e operazioni di rotazione. Le funzioni fix_insert e fix_remove garantiscono che le proprietà dell'albero rosso-nero siano mantenute dopo ogni inserimento o rimozione.
class RBTree(BST):
    def __init__(self, root = None):
        super().__init__(root)

    def insert(self, node):
        super().insert(node)
        node.color = "red"
        self.fix_insert(node)

    #remove rimuove un nodo dall'albero, gestendo i casi di nodi con due figli, un solo figlio o nessun figlio. Se il nodo rimosso è nero, chiama fix_remove per mantenere le proprietà dell'albero rosso-nero.
    def remove(self, node):
        if node.left is not None and node.right is not None:
            successor = self.nxt(node)
            node.key = successor.key
            node = successor
        if node.left is not None:
            child = node.left
        else:
            child = node.right
        if child is not None:
            child.parent = node.parent
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        if node.color == "black":
            self.fix_remove(child, node.parent)
    
    #fix_insert garantisce che le proprietà dell'albero rosso-nero siano mantenute dopo l'inserimento di un nodo. Gestisce i casi in cui il genitore del nodo inserito è rosso, eseguendo rotazioni e cambiamenti di colore per mantenere l'equilibrio dell'albero.
    def fix_insert(self, node):
        while node != self.root and color(node.parent) == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if color(uncle) == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if color(uncle) == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_left(node.parent.parent)
        self.root.color = "black"
        
    #fix_remove garantisce che le proprietà dell'albero rosso-nero siano mantenute dopo la rimozione di un nodo. Gestisce i casi in cui il nodo rimosso è nero, eseguendo rotazioni e cambiamenti di colore per mantenere l'equilibrio dell'albero.
    def fix_remove(self, node, parent):
        while node != self.root and color(node) == "black":
            if node == parent.left:
                sibling = parent.right
                if color(sibling) == "red":
                    sibling.color = "black"
                    parent.color = "red"
                    self.rotate_left(parent)
                    sibling = parent.right
                if color(sibling.left) == "black" and color(sibling.right) == "black":
                    sibling.color = "red"
                    node = parent
                    parent = node.parent
                else:
                    if color(sibling.right) == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.rotate_right(sibling)
                        sibling = parent.right
                    sibling.color = parent.color
                    parent.color = "black"
                    sibling.right.color = "black"
                    self.rotate_left(parent)
                    node = self.root
            else:
                sibling = parent.left
                if color(sibling) == "red":
                    sibling.color = "black"
                    parent.color = "red"
                    self.rotate_right(parent)
                    sibling = parent.left
                if color(sibling.left) == "black" and color(sibling.right) == "black":
                    sibling.color = "red"
                    node = parent
                    parent = node.parent
                else:
                    if color(sibling.left) == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.rotate_left(sibling)
                        sibling = parent.left
                    sibling.color = parent.color
                    parent.color = "black"
                    sibling.left.color = "black"
                    self.rotate_right(parent)
                    node = self.root
        if node is not None:
            node.color = "black"
        
    def find(self, key):
        return super().find(key)
    
    def nxt(self, node):
        return super().nxt(node)
    
    def prv(self, node):
        return super().prv(node)
