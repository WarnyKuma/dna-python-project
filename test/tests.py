from src.dna_utils import *
import unittest


class TestDNATools(unittest.TestCase):

    def test_crop_sequence(self):
        self.assertEqual(crop_sequence("ATGCGTACGT", 3, 7), "CGTA")
        self.assertEqual(crop_sequence("ATGC", 0, 4), "ATGC")
        self.assertEqual(crop_sequence("ATGC", 1, 3), "TG")

    def test_find_pattern(self):
        self.assertEqual(find_pattern("ATGCGTACGT", "CGT"), [3, 7])
        self.assertEqual(find_pattern("AAAAAA", "AA"), [0, 1, 2, 3, 4])
        self.assertEqual(find_pattern("ATGCATGC", "GAC"), [])

    def test_translate_dna_to_protein(self):
        self.assertEqual(translate_dna_to_protein("ATGGCC"), "MA")
        self.assertEqual(translate_dna_to_protein("ATGTAA"), "M_")
        self.assertEqual(translate_dna_to_protein("ATGNNN"), "MX")  # 'NNN' is unknown codon
        self.assertEqual(translate_dna_to_protein(""), "")
        self.assertEqual(translate_dna_to_protein("ATGCGTA"), "MR")  # Ignores last base 'A'

    def test_detect_mutations(self):
        self.assertEqual(
            detect_mutations("ATGC", "ATGT"),
            ["Substitution at position 4: C -> T"]
        )
        self.assertEqual(
            detect_mutations("ATGCGT", "ATGC"),
            ["Deletion at position 5: GT"]
        )
        self.assertEqual(
            detect_mutations("ATGC", "ATGCGG"),
            ["Insertion at position 5: GG"]
        )
        self.assertEqual(
            detect_mutations("ATGC", "ATGC"),
            []
        )


if __name__ == '__main__':
    unittest.main()
