# CAF sample app

A deterministic Python 3.12+ order quoting library used as the coding target for CAF experiments. It has no runtime dependencies, services, credentials, or network calls. This is a fixture, not a CAF service.

The baseline implementation computes a merchandise subtotal and shipping in integer cents. Orders of at least 5,000 cents ship free; a smaller nonempty order costs 500 cents to ship. See [`tasks/discount-code.md`](tasks/discount-code.md) for a reproducible agent task and acceptance criteria.

Run from this repository root:

```sh
uv run --offline python -m unittest discover -s tests -p 'test_baseline.py'
uv run --offline python -m unittest discover -s tests -p 'test_discount_code.py'
```

At the fixture base commit, the baseline suite passes and the discount-code suite intentionally fails. The latter is the coding objective. No CAF runtime or external coding CLI behavior is implied by this fixture.
