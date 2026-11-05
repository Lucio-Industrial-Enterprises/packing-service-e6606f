import unittest

from warehouse.sku import normalize_sku


class SkuTests(unittest.TestCase):
    def test_canonical_sku(self):
        for value in (" a-12 ", "a-12", "A-12", "\t a-12\n"):
            with self.subTest(value=value):
                self.assertEqual(normalize_sku(value), "A-12")

    def test_mixed_case_sku(self):
        self.assertEqual(normalize_sku(" aB-12c "), "AB-12C")

    def test_blank_sku(self):
        for value in ("", "  ", "\t\n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_sku(value)
