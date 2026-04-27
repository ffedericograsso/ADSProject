from ExperimentSetup import ExperimentSetup
from ExperimentRunner import ExperimentRunner

def main():
    print("Inizializzazione del setup degli esperimenti...")
    setup = ExperimentSetup(min_n=1000, max_n=10000000, steps=100)
    
    print("Avvio del runner...")
    runner = ExperimentRunner(setup)
    runner.run_experiments()
    
    risultati = runner.get_results()
    print("Esperimenti completati! Risultati:\n (DA FARE)")

if __name__ == "__main__":
    main()