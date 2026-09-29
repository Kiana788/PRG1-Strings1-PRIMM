# Stretch 1: Method chaining

File: `chaining.py`

Optional. Only if you have finished the four core activities.

## Predict

The first three lines apply the same three methods to the same string, in
different orders. Write down all three outputs before running.

## Run

Execute it. Two of the three agree. One does not.

## Investigate

- Which ordering gave a different answer, and why did the other two agree?
- Work out what the string looks like after each step of the odd one out. Write
  the intermediate values down rather than reasoning about it in your head.
- In the second block, `.strip()` is applied to each name after splitting rather
  than to the whole string before. What would go wrong if you stripped first and
  split second?

## Modify

- Add `.replace(" ", "")` somewhere in the first chain. Predict where it makes a
  difference and where it makes none.

> Chained methods run left to right, and each one works on whatever the previous
> one handed back. Reading a chain means reading it in that order, one step at a
> time.
