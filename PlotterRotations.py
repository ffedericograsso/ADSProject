import matplotlib.pyplot as plt
import sys
import random

sys.path.append(".")
from project import Project

def run_rotations_benchmark():
    # Valori di N per cui calcolare il numero di rotazioni
    N_values = [1000, 5000, 10000, 25000, 50000, 75000, 100000]
    
    structures = ["BST", "AVL", "RBT"]
    results = {struct: [] for struct in structures}
    
    print("Avvio estrazione conteggio rotazioni...")
    
    for struct_name in structures:
        print(f"Contando le rotazioni per {struct_name}...")
        for n in N_values:
            # Creiamo l'albero e la factory dei nodi
            project = Project(struct_name, n)
            tree = project.tree
            
            # Inietta e forza l'inizializzazione del contatore a 0 per ogni albero
            tree.rotation_count = 0
            
            # Generiamo chiavi casuali per simulare il caso medio
            keys = list(range(n))
            random.shuffle(keys)
            
            # Popoliamo l'albero creando PRIMA il nodo (Fix dell'errore)
            for key in keys:
                node = project.create_node(key)
                tree.insert(node)
                
            # Recuperiamo il numero di rotazioni effettuate
            rotations = getattr(tree, 'rotation_count', 0)
            results[struct_name].append(rotations)
            
    # --- Generazione del Grafico ---
    plt.figure(figsize=(10, 6))
    color_map = {"BST": "blue", "AVL": "orange", "RBT": "red"}
    
    for struct_name in structures:
        plt.plot(N_values, results[struct_name], marker='D', markersize=4, linestyle='-', 
                 label=struct_name, color=color_map[struct_name])
                 
    plt.title('Rotazioni cumulative su input casuale', fontsize=14)
    plt.xlabel('Dimensione dell\'albero (N)', fontsize=12)
    plt.ylabel('Numero Totale di Rotazioni', fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend(fontsize=12)
    plt.tight_layout()
    
    plt.savefig("grafico_rotazioni.png", dpi=300)
    print("=> Grafico 'grafico_rotazioni.png' generato con successo!")
    plt.show()

if __name__ == "__main__":
    run_rotations_benchmark()