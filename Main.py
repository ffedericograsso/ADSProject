from ExperimentSetup import ExperimentSetup
from ExperimentRunner import ExperimentRunner
from Plotter import ResultPlotter

def main():
    print("Inizializzazione del setup degli esperimenti...")
    setup = ExperimentSetup(min_n=1000, max_n=10000000, steps=100)
    
    print("Avvio dell'esperimento...")
    runner = ExperimentRunner(setup, n_exp=10)
    runner.run_experiments()
    
    print("Esperimenti completati! Risultati:\n")
    risultati = runner.get_results()

    print("Plot del grafico:\n")
    plotter = ResultPlotter(risultati)
    plotter.plot_time_complexity()

if __name__ == "__main__":
    main()