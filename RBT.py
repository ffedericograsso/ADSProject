from BST import BST, TreeNode

# Restituisce il colore di un nodo, restituendo "black" se il nodo è None o se non ha un attributo "color". Altrimenti, restituisce il valore dell'attributo "color" del nodo.
def color(node):
    return getattr(node, "color", "black") if node != None else "black"


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
