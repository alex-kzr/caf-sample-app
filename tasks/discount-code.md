# Discount code coding task

## Reproducible input

Use the `caf-sample-app` repository at the `discount-code-base-v1` tag. Resolve its exact commit with `git rev-parse discount-code-base-v1` and record that SHA with every experiment. Work in a fresh Git worktree from that commit. Do not use credentials, network access, or external services.

Task prompt for the coding agent:

> Add an optional `discount_code: str | None = None` argument to `caf_sample.quote_order`. Support the code `SAVE10` in any letter case. It deducts 10% of the merchandise subtotal, rounded to the nearest whole cent with halves rounded up. Compute shipping from the original subtotal, before the discount. Unknown, empty, or whitespace-only codes must raise `ValueError`. `None` preserves current behavior. Return the discount in `Quote.discount_cents` and include it in the final total. Keep the current item validation and all existing behavior. Change implementation code and add any useful tests; do not edit the acceptance suite.

## Acceptance

- `tests/test_baseline.py` and `tests/test_discount_code.py` both pass.
- The `SAVE10` calculation uses integer cents; 105 cents yields an 11-cent discount.
- A 5,000-cent pre-discount subtotal still gets free shipping after the discount.
- All outcomes are deterministic and require no API, CLI agent, database, or container.

## Commands

```sh
uv run --offline python -m unittest discover -s tests -p 'test_baseline.py'
uv run --offline python -m unittest discover -s tests -p 'test_discount_code.py'
```

Before the coding change, the first command must pass and the second must fail because `quote_order` has no `discount_code` parameter. A successful coding change makes both pass. Use the same base commit for all experimental modes and record each mode's resulting commit separately.
