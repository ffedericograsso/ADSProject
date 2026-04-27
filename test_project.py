import unittest

# TestProject contiene unit test per la classe Project, verificando che l'inizializzazione, la creazione di nodi, e le modifiche alla struttura funzionino correttamente. I test coprono sia l'accettazione di nomi di strutture che di classi, e assicurano che vengano sollevate eccezioni per input non validi.
if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("tests")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)