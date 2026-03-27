# ADSProject
## Istruzioni Progetto
Implementare e confrontare due strutture dati:
- Binary Search Tree **semplici** (non bilanciati)
- Binary Search Tree **AVL**
- Binary Search Tree **Red-Black**

Per ogni struttura dati menzionata sarà necessario misurare sperimentalmente il **tempo medio di inserimento** di una nuova chiave quando l'albero contiene esattamente $n$ chiavi.
L'obiettivo è ottenere, per diversi valori di $n$, **stime robuste** dei tempi di esecuzione medi, che permettano di confrontare il comportamento osservato con la complessità teorica (ad esempio $O(\log n)$).

Sarà necessario ragionare su:
1. come costruire e operare su alberi in modo che mantengano una dimensione $n$ data;
2. come garantire che le misure siano statisticamente significative, cioè basate su molti alberi di forma diversa e di dimensione fissata $n$;
3. come mantenere il costo di inizializzazione ragionevole, in modo che l'esperimento sia eseguibile per diversi valori di $n$, anche molto grandi.

### Come misurare il tempo?
Utilizzo della funzione `perf_counter()` del modulo `time` di Python.
```py
import time

start = time.perf_counter()
...
stop = time.perf_counter()

duration = stop - start
```

Dopo aver indicato con $T(n)$ il tempo medio dell'operazione `insert(k)` applicata ad una delle strutture dati citate sopra con $n$ chiavi, dove `k` è una chiave non appartenente all'albero. Per stimare questo tempo medio:
1. **Dimensione controllata**:
Le operazioni di inserimento devono avvenire su alberi che devono contenere esattamente $n$ chiavi.
2. **Varietà di alberi**:
Le misure devono avvenire sempre su diversi alberi di dimensione $n$ (con distribuzione casuale delle forme). Dobbiamo trovare il tempo medio di inserimento $T(n)$ su alberi casuali con distribuzione uniforme!!
3. **Robustezza statistica**:
Per ogni $n$ dobbiamo avere un numero sufficiente di misure (decine), per poter calcolare medie, mediane, ecc., (riduzione rumore ;))
4. **Inizializzazione efficiente**:
Non ripetere inutilmente operazioni di costo $O(n)$ ogni volta che misuriamo un inserimento di costo $O(\log n)$. Invece si può avere una sola volta, per ogni istanza di $n$, il costo $O(n)$ se riutilizziamo l'albero nei successivi inserimenti.

### Idea da Implementare
Costruire, per ciascun valore di $n$, un albero di dimensione $n$ applicandone una sequenza di operazioni di inserimento e cancellazione che mantiene costante la dimensione dell'albero, ma che al tempo stesso ne cambia continuamente la forma.

**Algoritmo**:
Per una delle strutture dati da implementare e un valore $n$ dato, effettuare i seguenti passaggi:
- <u>Inizializzazione</u>:
Una sola volta (senza cronometrare):
    - Costruire un insieme di $n+1$ chiavi distinte (es.: $0, \dots,n$).
    - Costruire un albero spostando $n$ chiavi in modo casuale dall'insieme all'albero.
    
    L'albero avrà dimensione $n$ e una forma uniformemente distribuita fra i possibili alberi di dimensione $n$. Avremo ancora una chiave non ancora spostata dall'insieme all'albero.
- <u>Misurazioni</u>:
Eseguire misurazioni ripetute (es.:decine di volte). Per ogni misurazione:
    - Scegliere l'**unica chiave** $k$ rimasta e si misura il tempo per eseguire `insert(k)`. 
    - Poi, si sceglie casualmente una chiave presente nell'albero e la si **rimuove senza cronometrarne** l'operazione di cancellazione, poi la si reinserisce cronometrandone l'inserimento.

Sui tempi di ciascuna misurazione si calcoli una **mediana**. 

**Analisi**:
1. <u>Dimensione controllata</u>:
   Dopo ogni coppia insert-remove, l'albero avrà sempre esattamente $n$ chiavi. Ciò implica che, prima di ogni inserimento, l'albero abbia $n$ chiavi.
2. <u>Varietà degli alberi</u>:
   Ogni passo modifica la forma dell'albero, in quanto ogni inserimento e cancellazione avvengono su chiavi scelte casualmente e con distribuzione uniforme. Questo implica anche una distribuzione uniforme nella forma degli alberi di dimensione $n$ su cui verranno effettuati gli inserimenti. Dunque le misurazioni avverranno su un insieme ampio e vario di alberi.
3. <u>Robustezza statistica</u>:
   Possiamo generare molte misure con una sola inizializzazione. Le forme su cui misuriamo sono diverse, grazie al fatto che abbiamo operazioni casuali.
4. <u>Inizializzazione efficiente</u>:
   Costruiamo l'albero di dimensione $n$ una sola volta. Dopo ogni misurazione, il costo di cancellazione di una singola chiave, sarà pari a $O(\log n)$. In questo modo l'*overhead* per le diverse misurazioni è paragonabile ai tempi effettivamente misurati.

**Conclusione**:
L'algoritmo descritto soddisfa tutti e quattro i requisiti e sarà alla base del progetto di laboratorio.

### Selezione efficiente delle chiavi
Non fare tanti tentativi "a vuoto" (es.: generare interi casuali finché non si becca quella non presente), questo produrrebbe misurazioni inefficienti.
Si dovrà, obbligatoriamente, rappresentare gli insiemi di chiavi tramite array. La selezione di una chiave da uno dei due array avviene generando una posizione casuale nell'array e accedendo all'elemento in quella posizione. L'inserimento di una chiave in un array può avvenire in tempo costante scambiando la chiave stessa con 


















