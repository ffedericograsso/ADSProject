import random

'''
IDEA:
1. Dichiarazione di un array A di lunghezza n+1, assumere che A[i] = i per i = 0, 1, ..., n.
2. Dichiarazione di un intero m, che delimit il confine tra le chiavi usate e quelle disponibili (non usate). In questo modo:
    - A[0...m-1] contiene le chiavi già inserite nell'albero.
    - A[m...n] contiene le chiavi ancora disponibili, non ancora inserite nell'albero.
3. Se si volesse selezionare una chiave k da inserire, sarebbe sufficiente scegliere un indice i causale nell'intervallo [m..n], definire k=A[i] con A[m] e incrementare m di 1.
4. Per rimuovere una chiave k, basterebbe generare a caso un indice i nell'intervallo [0..m-1], definire k=A[i], scambiare A[i] con A[m] e decrementare m di 1.
'''

class KeyManager:
    def __init__(self, n):
        self.A = list(range(n+1))
        self.m = 0
        self.n = n
    
    def get_key_insert(self):
        if self.m > self.n:
            raise Exception("Tutte le chiavi sono state inserite.")
        
        # Scelta indice random tra m e n
        i = random.randint(self.m, self.n)
        k = self.A[i]

        # Scambia A[i] con A[m] e incrementa m di 1
        self.A[i], self.A[self.m] = self.A[self.m], self.A[i]
        self.m += 1

        return k
    
    def get_key_remove(self):
        if self.m == 0:
            raise Exception("Nessuna chiave fino ad ora inserita da rimuovere.")
        
        # Scelta indice random tra 0 e m-1
        i = random.randint(0, self.m - 1)
        k = self.A[i]


        # Scambia A[i] con A[m-1] e decremento m
        self.m -= 1
        self.A[i], self.A[self.m] = self.A[self.m], self.A[i]

        return k
    
    def get_used_keys(self):
        return self.A[:self.m]
    
    def get_available_keys(self):
        return self.A[self.m:]