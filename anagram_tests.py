"""
Testing for the anagram solver and input function
"""
import unittest

import anagram_solver

# Load dictionary for use in tests of anagram_solver.solveMultiple()
dictionary = anagram_solver.parse_dictionary("dictionary.txt")


class SolveMultipleTests(unittest.TestCase):

    def test_string_not_in_dict(self):
        output = anagram_solver.solve_multiple("fat", dictionary)
        self.assertEqual(output, [])

    def test_string_in_dict(self):
        output = anagram_solver.solve_multiple("rates", dictionary)
        self.assertEqual(output, ['tares', 'tarse', 'sater', 'tears', 'teras', 'serta', 'tresa', 'artes', 'aster', 'stare', 'strae'])

    def test_no_valid_anagrams(self):
        output = anagram_solver.solve_multiple("foul", dictionary)
        self.assertEqual(output, [])

    def test_alphabetical_by_2nd_letter(self):
        output = anagram_solver.solve_multiple("takes", dictionary)
        self.assertEqual(output, ['keast', 'skate', 'stake', 'steak'])

    def test_no_2nd_arg(self):
        with self.assertRaises(TypeError):
            output = anagram_solver.solve_multiple("argument")


class SolveOneTests(unittest.TestCase):

    def test_string_not_in_dict(self):
        output = anagram_solver.solve_one("fat")
        self.assertEqual(output, [])

    def test_string_in_dict(self):
        output = anagram_solver.solve_one("rates")
        self.assertEqual(output, ['tares', 'tarse', 'sater', 'tears', 'teras', 'serta', 'tresa', 'artes', 'aster', 'stare', 'strae'])

    def test_no_valid_anagrams(self):
        output = anagram_solver.solve_one("foul")
        self.assertEqual(output, [])

    def test_alphabetical_by_2nd_letter(self):
        output = anagram_solver.solve_one("takes")
        self.assertEqual(output, ['keast', 'skate', 'stake', 'steak'])


class ValidateInputTests(unittest.TestCase):

    def test_non_string_input(self):
        with self.assertRaises(AttributeError):
            output = anagram_solver.validate_input(9999)

    def test_non_alphabetic_string_input(self):
        output = anagram_solver.validate_input(")(*)*)*&^(*&^(*&^(*&^")
        self.assertEqual(output, False)

    def test_max_word_length(self):
        output = anagram_solver.validate_input("antidisestablishmentarianism")
        self.assertEqual(output, False)


class ParseDictionaryTests(unittest.TestCase):

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            output = anagram_solver.parse_dictionary("random.txt")

if __name__ == "__main__":
    unittest.main()
