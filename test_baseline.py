import unittest
from baseline import longest_cubic_subsequence


class TestBaseline(unittest.TestCase):
    def test_sequences(self):
        # Each input is paired with its acceptable answers.
        cases = [
            ("abc", [""]),
            ("aaa", ["aaa"]),
            ("aaaa", ["aaa"]),
            ("abcabcabc", ["abcabcabc"]),
            ("axbycabcabc", ["abcabcabc"]),
            ("aaabbbccc", ["aaa", "bbb", "ccc"]),
            ("", [""]),
        ]

        for sequence, expected in cases:
            with self.subTest(sequence=sequence):
                result = longest_cubic_subsequence(sequence)
                self.assertIn(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)