from unittest import TestCase
from scrabble import Scrabble


class TestScrabble(TestCase):
    def test_get_user_input(self):
        self.fail()

    def test_obligatory_check(self):
        test = Scrabble()
        t1 = test.obligatory_check('abcdefghij', 'abcdefghij')
        self.assertFalse(t1)
        t2 = test.obligatory_check('abcdefghij', 'yuv')
        self.assertTrue(t2)
        t3 = test.obligatory_check('abcdefghij', '')
        self.assertFalse(t3)

    def test_load_words(self):
        '''check if words are loaded correctly - check first and last word'''
        test = Scrabble().load_words()
        self.assertIn('aa', test)
        self.assertIn('zzzs', test)

    def test_find_possible_words(self):
        self.fail()

    def test_obligatory_words(self):
        self.fail()

    def test_assign_score(self):
        test = Scrabble()
        test.words = ['ahoj', 'underground', '']
        t1 = test.assign_score()
        self.assertEqual(t1, {'ahoj': 14, 'underground': 14, '': 0})

    def test_output(self):
        self.fail()

    def test_run(self):
        self.fail()
