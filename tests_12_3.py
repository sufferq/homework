import runner
import unittest
from runner_and_tournament import Tournament, Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner('Петя')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        run = runner.Runner('Аня')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        walker2 = runner.Runner('Артём')
        run2 = runner.Runner('Егор')
        for i in range(10):
            walker2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walker2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runners = [
            Runner("Усэйн", 10),
            Runner("Андрей", 9),
            Runner("Ник", 3),
        ]

    @classmethod
    def tearDownClass(cls):
        for tournament, results in cls.all_results.items():
            print(f'{tournament}: {{{', '.join([f'{place}: {name}' for place, name in results.items()])}}}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def __test_tournament(self, distance:int, *people:str):
        participants = [runner for runner in self.runners if runner in people]
        tournament = Tournament(distance, *participants)
        return tournament.start()

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        results = self.__test_tournament(90, 'Усэйн', 'Ник')
        self.all_results['1'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        results = self.__test_tournament(90, 'Андрей', 'Ник')
        self.all_results['2'] = results
        self.assertTrue(results[max(results)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        results = self.__test_tournament(90, 'Усэйн', 'Андрей', 'Ник')
        self.all_results['3'] = results
        self.assertTrue(results[max(results)] == 'Ник')


if __name__ == '__main__':
    unittest.main()
