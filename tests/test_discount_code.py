"""Acceptance tests for tasks/discount-code.md; expected to fail at the base commit."""

import unittest

from caf_sample import LineItem, Quote, quote_order


class DiscountCodeAcceptanceTests(unittest.TestCase):
    def test_ten_percent_rounds_half_up(self):
        self.assertEqual(
            quote_order([LineItem("pen", 105, 1)], discount_code="SAVE10"),
            Quote(105, 11, 500, 594),
        )

    def test_shipping_uses_original_subtotal(self):
        self.assertEqual(
            quote_order([LineItem("book", 5_000, 1)], discount_code="SAVE10"),
            Quote(5_000, 500, 0, 4_500),
        )

    def test_discount_code_is_case_insensitive(self):
        self.assertEqual(
            quote_order([LineItem("pen", 100, 1)], discount_code="save10"),
            Quote(100, 10, 500, 590),
        )

    def test_empty_order_with_discount(self):
        self.assertEqual(quote_order([], discount_code="SAVE10"), Quote(0, 0, 0, 0))

    def test_unknown_code_rejected(self):
        with self.assertRaises(ValueError):
            quote_order([LineItem("pen", 100, 1)], discount_code="OTHER")

    def test_blank_code_rejected(self):
        for code in ("", "   "):
            with self.subTest(code=code), self.assertRaises(ValueError):
                quote_order([LineItem("pen", 100, 1)], discount_code=code)

    def test_no_code_preserves_baseline(self):
        self.assertEqual(
            quote_order([LineItem("pen", 100, 1)], discount_code=None),
            Quote(100, 0, 500, 600),
        )


if __name__ == "__main__":
    unittest.main()
