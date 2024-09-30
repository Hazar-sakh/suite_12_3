import unittest
import Runner
import Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        c = Runner.Runner('Dobrynya')
        for i in range(10):
            c.walk()
        self.assertEqual(c.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        golo = Runner.Runner('Alyosha')
        for i in range(10):
            golo.run()
        self.assertEqual(golo.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        giga = Runner.Runner('Yarilo')
        mega = Runner.Runner('Veles')
        for i in range(10):
            giga.run()
            mega.walk()
        self.assertNotEqual(giga.distance, mega.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    def setUp(self):
        self.U = Tournament.Runner('Усейн', 10)
        self.A = Tournament.Runner('Андрей', 9)
        self.N = Tournament.Runner('Ник', 3)

    def resulter(self, args):
        res = []
        for key, value in args.items():
            res.append((key, str(value)))
        all_results.update(res)
        print(self.tearDownClass())

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        d1 = Tournament.Tournament(90, self.U, self.N)
        r1 = d1.start()
        self.resulter(r1)
        self.assertTrue(r1[2] == 'Ник', f'Ошибка: {r1[1]} не может быть последним!')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        d2 = Tournament.Tournament(90, self.A, self.N)
        r2 = d2.start()
        self.resulter(r2)
        self.assertTrue(r2[2] == 'Ник', f'Ошибка: {r2[1]} не может быть последним!')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        d3 = Tournament.Tournament(90, self.U, self.A, self.N)
        r3 = d3.start()
        self.resulter(r3)
        self.assertTrue(r3[3] == 'Ник', f'Ошибка: {r3[3]} не может быть последним!')

    #ДОПОЛНИТЕЛЬНО
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_4(self):
        d4 = Tournament.Tournament(6, self.U, self.A, self.N)
        r4 = d4.start()
        self.resulter(r4)
        self.assertTrue(r4[3] == 'Ник', f'Ошибка: {r4[3]} не может быть последним!')

    @classmethod
    def tearDownClass(cls):
        return all_results


if __name__ == '__main__':
    unittest.main