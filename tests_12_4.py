import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            walker = Runner('Петя', -5)
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run = Runner(352627)
            for i in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Невереный тип данных лоя объекта Runner', exc_info=True)

    def test_challenge(self):
        walker2 = Runner('Артём')
        run2 = Runner('Егор')
        for i in range(10):
            walker2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walker2.distance)

if __name__ == '__main__':
    unittest.main()