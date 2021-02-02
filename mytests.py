import unittest
from mycode import get_greetings, Rick, Morty, Citadel


""" Basice unittest implementation """


class FirstTestClass(unittest.TestCase):
    # tests checks if the output is uppsercase
    def test_upper(self):
        self.assertEqual('rubiks code'.upper(), 'RUBIKS CODE')


class HelloWorldTest(unittest.TestCase):
    # test extends get_greetings function and compares the output
    def test_get_helloworld(self):
        self.assertEqual(get_greetings(), 'Hello World!')


""" Unittest implemented in Rick and Morty game """


class RickTest(unittest.TestCase):

    def test_universe(self):
        rick = Rick(111)
        self.assertEqual(rick.universe, 111)

    def test_has_morty(self):
        rick = Rick(111)
        self.assertEqual(rick.morty, None)

    def test_assign_morty(self):
        rick = Rick(111)
        morty = Morty(111)

        rick.assign(morty)

        self.assertEqual(rick.morty, morty)
        self.assertTrue(morty.is_assigned)

    def test_has_is_pickle(self):
        rick = Rick(111)
        self.assertFalse(rick.is_pickle)


class MortyTest(unittest.TestCase):

    def test_universe(self):
        morty = Morty(111)
        self.assertEqual(morty.universe, 111)

    def test_is_assigned(self):
        morty = Morty(111)
        self.assertFalse(morty.is_assigned)


class CitadelTest(unittest.TestCase):

    def test_get_all_residents(self):
        citadel = Citadel()
        residents = citadel.get_all_residents()
        self.assertCountEqual(residents, [])

    def test_add_residents(self):
        citadel = Citadel()
        rick = Rick(111)
        morty = Morty(111)

        citadel.add_resident(rick)
        citadel.add_resident(morty)
        residents = citadel.get_all_residents()

        self.assertEqual(residents[0], rick)
        self.assertEqual(residents[1], morty)

    def test_pickle_ricks_with_morties(self):
        citadel = Citadel()
        rick = Rick(111)
        morty = Morty(111)
        rick.assign(morty)

        citadel.add_resident(rick)
        citadel.add_resident(morty)

        citadel.pickle_ricks_with_morties()
        residents = citadel.get_all_residents()

        self.assertTrue(residents[0].is_pickle)




if __name__ == '__main__':
    unittest.main()