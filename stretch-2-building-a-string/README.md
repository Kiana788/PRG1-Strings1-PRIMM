# Stretch 2: Building a string

File: `building.py`

Optional. Only if you have finished the four core activities.

Two programs that construct a new string rather than picking one apart.

## Predict

- What does `initials_of("ada byron lovelace")` return?
- What does `initials_of("Grace Hopper")` return?
- What does the redaction line print?

## Run

Execute and compare.

## Investigate

- `initials` starts as `""`. Why not `" "` or `"."`? This is the same question
  as an accumulator starting at 0 rather than 1, which you met with loops.
- Trace `initials_of("Grace Hopper")` by hand: write down what `initials` holds
  after each pass.
- `"*" * len(secret)` produces a run of stars. What does the `*` operator do
  when one side is a string and the other is a number?
- `redact` uses `.replace`, which replaces **every** occurrence. When would that
  be exactly what you want, and when would it be a fault?

## Modify

- Make `initials_of` skip any word shorter than two characters, so a stray
  initial in the input does not produce a doubled full stop.
- Make `redact` leave the last four characters visible, the way a bank does with
  a card number.

> Building a string across a loop is the same accumulator pattern you met on
> Day 3, with a different starting value and a different operator.
