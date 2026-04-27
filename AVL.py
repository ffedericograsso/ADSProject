# Implementazione di un albero AVL, che estende un albero binario di ricerca (BST) con bilanciamento automatico.
# class TreeNode rappresenta un nodo generico dell'albero, con chiave, puntatori a sinistra e destra, e un puntatore al genitore.
# La classe AVL estende la classe BST.
from platform import node


class TreeNode:
    # Inizializza un nodo con una chiave e opzionalmente con figli sinistro e destro. Imposta anche il puntatore al genitore.
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        if left is not None:
            left.parent = self
        if right is not None:
            right.parent = self

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

#La classe BST implementa un albero binario di ricerca con operazioni di inserimento, rimozione, rotazione e ricerca. La classe AVL estende BST aggiungendo il bilanciamento automatico dopo ogni inserimento o rimozione, garantendo che l'albero rimanga bilanciato.
class BST:
    #init inizializza l'albero con una radice opzionale.
    def __init__(self, root = None):
        self.root = root
    
    #str fornisce una rappresentazione stringa dell'albero, mostrando la chiave di ogni nodo e i suoi figli.
    def __str__(self):
        if self.root == None:
            return "NULL "
        else:
            return f"{self.root.key} " + BST(self.root.left).__str__() + BST(self.root.right).__str__()

    #find cerca un nodo con una chiave specifica nell'albero, restituendo il nodo se trovato o None se non presente.
    def find(self, key):
        if self.root is None:
            return None
        if self.root.key == key:
            return self.root
        elif key < self.root.key:
            return BST(self.root.left).find(key)
        else:
            return BST(self.root.right).find(key)
        
    #nxt restituisce il nodo successore di un dato nodo, ovvero il nodo con la chiave più piccola maggiore di quella del nodo dato.
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
        
    #min restituisce il nodo con la chiave più piccola in un sottoalbero dato.
    def min(self, node):
        while node.left is not None:
            node = node.left
        return node

    #prv restituisce il nodo predecessore di un dato nodo, ovvero il nodo con la chiave più grande minore di quella del nodo dato.
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

    #max restituisce il nodo con la chiave più grande in un sottoalbero dato.
    def max(self, node):
        while node.right is not None:
            node = node.right
        return node
    
    #insert aggiunge un nuovo nodo all'albero, mantenendo la proprietà di albero binario di ricerca.
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

    #remove elimina un nodo dall'albero, mantenendo la proprietà di albero binario di ricerca. Gestisce i casi in cui il nodo da rimuovere ha due figli, un solo figlio o nessun figlio.
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

    #rotate_right esegue una rotazione a destra attorno a un nodo specificato, modificando la struttura dell'albero per mantenere le proprietà di bilanciamento.
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
    
    