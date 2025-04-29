KEEPFILTERS is a modifier, not a standalone function.
You can only use KEEPFILTERS inside a filter argument of CALCULATE or CALCULATETABLE; it can’t wrap an entire table expression on its own.

KEEPFILTERS makes filters additive (intersecting) instead of replacing.
By default, CALCULATE(…, Column = Value) replaces any existing filter on Column. Wrapping that predicate in KEEPFILTERS forces DAX to intersect it with whatever filters are already in place.
KEEPFILTERS syntax is simple.

dax
CALCULATE(
  <expression>,
  KEEPFILTERS( <BooleanFilter1> [, <BooleanFilter2>, … ] )
)
KEEPFILTERS shines in part-to-whole calculations.
Use KEEPFILTERS when you need “this item’s sales ÷ its category’s sales”—it preserves the category filter while applying your item filter.

KEEPFILTERS protects nested security or business rules.
When you have an RLS or broad rule on a table, KEEPFILTERS ensures your measure’s extra restrictions don’t accidentally remove that outer rule.

KEEPFILTERS supports multiple predicates.
You can pass several comma-separated Boolean tests into KEEPFILTERS, and each one will be intersected both with each other and with the external context.

KEEPFILTERS vs. ALL/REMOVEFILTERS (and other modifiers).
While ALL or REMOVEFILTERS clears filters, and ALLEXCEPT/ALLSELECTED clear selectively, KEEPFILTERS does the opposite—it retains existing filters and narrows them further.

KEEPFILTERS can outperform FILTER(...) for simple column predicates.
For straight column comparisons (e.g. Dim[Category] = "X"), KEEPFILTERS often lets the engine optimize better than wrapping a FILTER() over the entire table.

KEEPFILTERS returns BLANK when there’s no overlap.
If your outer context excludes every value in your KEEPFILTERS set, the measure will come back blank—no rows remain after intersection.