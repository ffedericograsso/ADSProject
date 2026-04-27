# Implementazione di un albero AVL, che estende un albero binario di ricerca (BST) con bilanciamento automatico.
# class TreeNode rappresenta un nodo generico dell'albero, con chiave, puntatori a sinistra e destra, e un puntatore al genitore.
# La classe AVL estende la classe BST.

from platform import node
from BST import BST, TreeNode

#height calcola l'altezza di un nodo, memorizzandola per evitare ricalcoli ridondanti. Se l'altezza è già calcolata, la restituisce direttamente.   
def height(node):
    if node == None:
        return 0
    if getattr(node, "height", None) is None:
        node.height = 1 + max(height(node.left), height(node.right))
    return node.height

#invalidate_height invalida l'altezza di un nodo e di tutti i suoi antenati, forzando il ricalcolo dell'altezza quando necessario.
def invalidate_height(node):
        while node != None:
            node.height = None
            node = node.parent


# La classe AVL estende la classe BST, aggiungendo funzionalità per mantenere l'albero bilanciato dopo ogni inserimento o rimozione. Utilizza le funzioni height e invalidate_height per gestire l'altezza dei nodi e la funzione rebalance per eseguire le rotazioni necessarie per mantenere l'equilibrio dell'albero.
class AVL(BST):
    def __init__(self, root = None):
        super().__init__(root)

    def insert(self, node):
        super().insert(node)
        invalidate_height(node)
        self.rebalance(node)

    def remove(self, node):
        super().remove(node)
        invalidate_height(node)
        self.rebalance(node.parent)

    #rebalance controlla l'equilibrio dell'albero a partire da un nodo specificato e esegue le rotazioni necessarie per mantenere l'albero bilanciato. Gestisce i casi di sbilanciamento a sinistra e a destra, identificando i pivot e i figli coinvolti nelle rotazioni.
    def rebalance(self, node):
        while node is not None:
            balance = height(node.left) - height(node.right)
            if balance > 1:
                pivot = node
                child = node.left
                if height(node.left.left) >= height(node.left.right):
                    self.rotate_right(pivot)
                    pivot.height = None
                    child.height = None
                else:
                    grandchild = node.left.right
                    self.rotate_left(child)
                    self.rotate_right(pivot)
                    pivot.height = None
                    child.height = None
                    grandchild.height = None
            elif balance < -1:
                pivot = node
                child = node.right
                if height(node.right.right) >= height(node.right.left):
                    self.rotate_left(pivot)
                    pivot.height = None
                    child.height = None
                else:
                    grandchild = node.right.left
                    self.rotate_right(child)
                    self.rotate_left(pivot)
                    pivot.height = None
                    child.height = None
                    grandchild.height = None
            
            node.height = None 
            node = node.parent
    
    def find(self, key):
        return super().find(key)
    
    def nxt(self, node):
        return super().nxt(node)
    
    def prv(self, node):
        return super().prv(node)
    
    