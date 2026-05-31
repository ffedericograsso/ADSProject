import matplotlib.pyplot as plt
import sys
import random

# Assicuriamo l'inclusione dei moduli
sys.path.append(".")
from Project import Project

def run_rotations_benchmark():
    N_values = [1000, 5000, 10000, 25000, 50000, 75000, 100000]
    
    structures = ["BST", "AVL", "RBT"]
    results = {struct: [] for struct in structures}
    
    print("Avvio estrazione conteggio rotazioni...")
    
    for struct_name in structures:
        print(f"Contando le rotazioni per {struct_name}...")
        for n in N_values:
            project = Project(struct_name, n)
            tree = project.tree
            
            if hasattr(tree, 'rotation_count'):
                tree.rotation_count = 0
            
            keys = list(range(n))
            random.shuffle(keys)
            
            for key in keys:
                tree.insert(key)
                
            rotations = getattr(tree, 'rotation_count', 0)
            results[struct_name].append(rotations)
            
    plt.figure(figsize=(10, 6))
    color_map = {"BST": "blue", "AVL": "orange", "RBT": "red"}
    
    for struct_name in structures:
        plt.plot(N_values, results[struct_name], marker='D', markersize=4, linestyle='-', 
                 label=struct_name, color=color_map[struct_name])
                 
    plt.title('Costo di Manutenzione: Rotazioni cumulative su input casuale', fontsize=14)
    plt.xlabel('Dimensione dell\'albero (N)', fontsize=12)
    plt.ylabel('Numero Totale di Rotazioni', fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend(fontsize=12)
    plt.tight_layout()
    
    plt.savefig("grafico_rotazioni.png", dpi=300)
    print("=> Grafico 'grafico_rotazioni.png' generato!")
    plt.show()

if __name__ == "__main__":
    run_rotations_benchmark()