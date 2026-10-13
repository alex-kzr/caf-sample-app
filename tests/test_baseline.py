import unittest

from caf_sample import LineItem, Quote, quote_order


class BaselineQuoteTests(unittest.TestCase):
    def test_empty_order(self):
        self.assertEqual(quote_order([]), Quote(0, 0, 0, 0))

    def test_paid_shipping_below_threshold(self):
        self.assertEqual(
            quote_order([LineItem("mug", 1_499, 2)]),
            Quote(2_998, 0, 500, 3_498),
        )

    def test_free_shipping_at_threshold(self):
        self.assertEqual(
            quote_order([LineItem("book", 2_500, 2)]),
            Quote(5_000, 0, 0, 5_000),
        )

    def test_multiple_items(self):
        self.assertEqual(
            quote_order([LineItem("pen", 125, 3), LineItem("pad", 300, 2)]),
            Quote(975, 0, 500, 1_475),
        )

    def test_invalid_items(self):
        invalid = [
            LineItem("", 100, 1), LineItem("sku", -1, 1),
            LineItem("sku", 100, 0), LineItem("sku", True, 1),
            LineItem("sku", 100, False),
        ]
        for item in invalid:
            with self.subTest(item=item), self.assertRaises(ValueError):
                quote_order([item])


if __name__ == "__main__":
    unittest.main()
