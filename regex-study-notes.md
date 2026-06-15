# Regex Study Notes

Flashcard-style reference covering fundamentals through advanced concepts. Each entry is a quick hit — bold term, then the explanation. Extra weight on the advanced corners and the gotchas that came up most.

---

## Core Building Blocks


`.` (the dot)
 — Matches any single character *except* a newline (by default). To match a literal period, escape it (`\.`) or put it in a class (`[.]`). Inside a character class, the dot loses its power and is just a literal dot.

<div align="center">• • •</div>


Character class `[ ]`
 — Matches exactly 
one
 character from the set inside. `[aeiou]` matches a single vowel, not all five. Ranges use a hyphen: `[a-z]`, `[A-Z]`, `[0-9]`.

<div align="center">• • •</div>


Negated class `[^ ]`
 — A `^` as the *first* character inside the brackets flips the meaning: `[^0-9]` matches any single character that is 
not
 a digit. (A `^` outside brackets is an anchor — different job.)

<div align="center">• • •</div>


Special chars go literal inside `[ ]`
 — Inside a class, `.`, `*`, `+`, `?`, `(`, `)`, `$` are just themselves. The only characters that stay special inside a class are `]` (closes it), `\` (escape), `^` (negation, only when first), and `-` (range, except when first/last).

---

## Shorthand Classes


`\d` / `\D`
 — `\d` = any digit, equivalent to `[0-9]`. `\D` = any non-digit. 
Gotcha:
 `\d` is digits *only* — it does NOT match hex letters. For hex use `[0-9a-fA-F]`.

<div align="center">• • •</div>


`\w` / `\W`
 — `\w` = word character, equivalent to `[a-zA-Z0-9_]` (note the underscore!). `\W` = any non-word character.

<div align="center">• • •</div>


`\s` / `\S`
 — `\s` = any whitespace (space, tab, newline, etc.). `\S` = any non-whitespace.

---

## Quantifiers


`*` `+` `?`
 — `*` = zero or more, `+` = one or more, `?` = zero or one (optional). `*` and `?` can match nothing, so they can match an empty string. `colou?r` matches both `color` and `colour`.

<div align="center">• • •</div>


`{n}` `{n,}` `{n,m}`
 — Counted repetition. `\d{4}` = exactly 4 digits. `\d{2,}` = 2 or more. `\d{2,4}` = between 2 and 4. 
Braces take numbers only
 — `{d}` is invalid (a common typo for `{2}`).

<div align="center">• • •</div>


A quantifier applies to the token immediately before it
 — In `ab+`, the `+` applies only to the `b`, not to `ab`. To repeat a sequence, group it: `(ab)+`.

<div align="center">• • •</div>


Greedy vs. Lazy
 — Quantifiers are 
greedy
 by default: they match as much as possible, then backtrack if needed. Add `?` to make them 
lazy
 (match as little as possible). On `<a><b>`: greedy `<.+>` grabs the whole `<a><b>`; lazy `<.+?>` grabs just `<a>`.

<div align="center">• • •</div>


Possessive `++` `*+` `?+`
 — Like greedy, but 
never gives characters back
 during backtracking. Prevents catastrophic backtracking. (Python's built-in `re` only supports these from version 3.11+.)

---

## Anchors & Boundaries


`^` and `$`
 — `^` = start of string, `$` = end of string. They are 
zero-width
: they assert a *position* and consume no characters. With the `m` (multiline) flag, they match the start/end of each *line*.

<div align="center">• • •</div>


Validate vs. Extract — the anchor rule
 ⭐ — To 
validate
 that an entire string matches, anchor both ends: `^...$`. Without anchors, the pattern only needs to match *somewhere* inside, so `\d{5}` happily matches the first 5 digits of `968131234`. To 
find/extract
 within larger text, leave anchors off.

<div align="center">• • •</div>


`\b` word boundary
 — A zero-width position between a word char (`\w`) and a non-word char. `\bcat\b` matches `cat` as a whole word but not inside `category`. 
Gotcha:
 `\b` only works *next to a word character* — placing it against a symbol like `#`, `@`, or `$` often backfires, because two non-word characters in a row have no boundary between them. (`#\w+` works; `\b#\w+` doesn't.)

<div align="center">• • •</div>


`\B` non-word boundary
 — The opposite of `\b`. `\Bcat\B` matches `cat` only when it's *inside* a word, like `scatter`.

---

## Groups & Alternation


Capturing group `( )`
 — Groups part of a pattern AND remembers (captures) what it matched for later reuse or extraction. Wrap the part you want to pull out: `"([^"]*)"` captures the text inside quotes.

<div align="center">• • •</div>


Non-capturing group `(?:...)`
 — Groups without capturing — no group number assigned. Use it for "I need to group these for a quantifier or alternation, but I don't need the captured text." Slightly more efficient and keeps your group numbers clean.

<div align="center">• • •</div>


Group numbering
 ⭐ — Capturing groups are numbered by the left-to-right order of their 
opening `(`
, counting *only* capturing groups. Non-capturing `(?:...)` groups are skipped. In `(\d{4})-(?:\d{2})-(\d{2})`, group 1 = year, group 2 = 
day
 (the `(?:...)` month is not numbered).

<div align="center">• • •</div>


Named group
 — Python: `(?P<name>...)`. .NET / JavaScript / PCRE / Java: `(?<name>...)`. Lets you refer to a group by name instead of number. 
The `P` is mandatory and Python-specific
 — `(?<name>)` is *not* valid in Python's standard `re`.

<div align="center">• • •</div>


Alternation `|`
 — The OR operator, with the 
lowest precedence
 of all regex operators. `^cat|dog$` means "starts with `cat`" OR "ends with `dog`" — not "`cat` or `dog` as whole strings." Wrap it to scope it: `^(cat|dog)$`.

<div align="center">• • •</div>


Ordered alternation
 — Branches are tried 
left to right
, and the *first* one that succeeds wins (it does NOT prefer the longest). `(a|ab)` against `ab` captures just `a`.

---

## Backreferences


Backreference `\1`, `\2`...
 — Re-matches the *exact text* a previous capturing group matched. `(\w+)\s+\1` finds a doubled word like `the the`. Distinct from `\d` — `\1` is "group 1's text," not "a digit."

<div align="center">• • •</div>


Named backreference
 — Python: `(?P=name)`. Others: `\k<name>`.

<div align="center">• • •</div>


Backreference gotcha — require your separators
 — In `(\w+)\s?\1`, the optional `\s?` lets a single word like `papa` or `byebye` match as `pa`+`pa`. Use `\s+` (required) and `\b` boundaries: `\b(\w+)\s+\1\b`.

---

## Lookaround (Zero-Width Assertions)


Positive lookahead `(?=X)`
 — Asserts "what follows is X" without consuming it. `\d+(?= USD)` matches `100` in `100 USD` but leaves ` USD` out of the match.

<div align="center">• • •</div>


Negative lookahead `(?!X)`
 — Asserts "what follows is NOT X." `\d+(?! USD)` matches a number *not* followed by ` USD`.

<div align="center">• • •</div>


Lookbehind `(?<=X)` / `(?<!X)`
 — Positive/negative versions that check what comes *before* the current position. `(?<=@)\w+` matches `domain` in `user@domain`.

<div align="center">• • •</div>


Stacked lookaheads — the password idiom
 ⭐ — Because lookaheads are zero-width (they rewind to the same position), you can stack several at the start, each checking one independent "must contain" rule:
```
^(?=.*\d)(?=.*[A-Z])(?=.*[!@#%]).{8,}$
```
= at least one digit AND one uppercase AND one special char AND 8+ chars total. 
Each rule needs its own `.*`
 — `(?=.*X)` means "contains X anywhere"; `(?=X)` without the `.*` pins X to the current position.

---

## Flags / Modifiers


`i` — case-insensitive
 — `/cat/i` matches `CAT`. Inline form: `(?i)` at the start, or scoped `(?i:...)`. 
Default behavior is case-SENSITIVE
 across all major engines (Python, JS, Java, .NET, PCRE, Ruby, Go).

<div align="center">• • •</div>


`g` — global
 — Find all matches, not just the first. (JavaScript flag; in Python this is the difference between `findall`/`finditer` and `search`.)

<div align="center">• • •</div>


`m` — multiline
 — Makes `^` and `$` match start/end of each *line*. Do not confuse with `s`.

<div align="center">• • •</div>


`s` — dotall / single-line
 — Makes `.` match newlines too. (The name is confusing — `s` is for "single line treated as one blob.")

<div align="center">• • •</div>


`x` — verbose / extended
 — Ignores literal whitespace in the pattern (so you can space things out for readability) and allows `#` comments. 
This is the ONLY mode where spaces in your pattern are ignored
 — normally whitespace is a literal character you have to match.

---

## Replacement / Substitution


Inserting a captured group in a replacement
 — Python `re.sub`: `\1` or the explicit `\g<1>` (use `\g<1>` when a literal digit follows, e.g. `\g<1>0`). JavaScript: `$1`. The `&1` / `%1` forms are sed/shell-flavored, not standard regex.

---

## Performance Trap


Catastrophic backtracking (ReDoS)
 ⭐ — Nested quantifiers like `(a+)+`, `(x*)*`, or `(a+)*` can blow up exponentially on long non-matching input (e.g. `^(a+)+$` against `"aaaaaaaa!"`), because the engine tries astronomically many ways to split the characters. 
Fixes:
 atomic groups `(?>...)` or possessive quantifiers `a++` remove the backtracking; or restructure the pattern to avoid the nesting. Be suspicious whenever you see a quantifier wrapped around another quantified token.

<div align="center">• • •</div>


Atomic group `(?>...)`
 — Once it matches, the engine 
won't backtrack into it
. A key tool against catastrophic backtracking.

---

## Quick-Reference: Common Patterns

| Target | Pattern |
|---|---|
| US ZIP (validate) | `^\d{5}(?:-\d{4})?$` |
| Hashtag (extract) | `#\w+` |
| 24-hour time `HH:MM` | `^(?:[01]\d\|2[0-3]):[0-5]\d$` |
| Hex color | `^#(?:[0-9a-fA-F]{3}\|[0-9a-fA-F]{6})$` |
| Quoted string contents | `"([^"]*)"` |
| Doubled word | `\b(\w+)\s+\1\b` |
| Password policy | `^(?=.*\d)(?=.*[A-Z]).{8,}$` |
| ISO date (named groups) | `(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})` |
| Email (loose) | `^[^\s@]+@[^\s@]+\.[^\s@]+$` |
| IPv4 (loose) | `\b(?:\d{1,3}\.){3}\d{1,3}\b` |

---

## Your Recurring Gotchas (the 4 to burn in)

1. 
Anchor when validating
 (`^...$`); leave anchors off when extracting.
2. 
Whitespace is literal
 in a pattern — unless you've turned on the `x`/verbose flag.
3. 
Match the right character set
 — `\d` is digits only; hex needs `[0-9a-fA-F]`, "text inside quotes" needs `[^"]`.
4. 
`\b` only works next to a word character
 — not against `#`, `@`, or `$`.
