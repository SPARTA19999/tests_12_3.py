import unittest
import tests_12_3

class TestSuite(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
        self.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    ts = unittest.TestSuite()
    runner.run(ts)

