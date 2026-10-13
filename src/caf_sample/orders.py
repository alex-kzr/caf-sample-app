"""Small, self-contained order quotation domain for coding benchmarks."""

from dataclasses import dataclass

FREE_SHIPPING_THRESHOLD_CENTS = 5_000
STANDARD_SHIPPING_CENTS = 500


@dataclass(frozen=True)
class LineItem:
    sku: str
    unit_price_cents: int
    quantity: int


@dataclass(frozen=True)
class Quote:
    subtotal_cents: int
    discount_cents: int
    shipping_cents: int
    total_cents: int


def quote_order(items: list[LineItem]) -> Quote:
    """Quote an order, with free shipping at a subtotal of at least 5,000 cents."""
    subtotal_cents = 0
    for item in items:
        if not item.sku:
            raise ValueError("SKU must not be empty")
        if isinstance(item.unit_price_cents, bool) or not isinstance(item.unit_price_cents, int):
            raise ValueError("unit price must be an integer number of cents")
        if isinstance(item.quantity, bool) or not isinstance(item.quantity, int):
            raise ValueError("quantity must be an integer")
        if item.unit_price_cents < 0 or item.quantity <= 0:
            raise ValueError("unit price must be nonnegative and quantity positive")
        subtotal_cents += item.unit_price_cents * item.quantity

    shipping_cents = (
        0 if not items or subtotal_cents >= FREE_SHIPPING_THRESHOLD_CENTS
        else STANDARD_SHIPPING_CENTS
    )
    return Quote(
        subtotal_cents=subtotal_cents,
        discount_cents=0,
        shipping_cents=shipping_cents,
        total_cents=subtotal_cents + shipping_cents,
    )
