# Stretch 1: Method chaining

File: `chaining.py`

Optional. Only if you have finished the four core activities.

## Predict

The first three lines apply the same three methods to the same string, in
different orders. Write down all three outputs before running.
The Hangover
The Hangover
the hangover
---
[Ada]
[Grace]
[Alan]

## Run

Execute it. Two of the three agree. One does not.

## Investigate

- Which ordering gave a different answer, and why did the other two agree? The third chain differs. Steps: title() first gives " The Hangover " (title also strips nothing, the spaces survive and get capitalised as nothing), then .strip() cleans it, then .lower() lowers everything, ending lowercase. The first two both end with .title(), which re-capitalises after cleaning, so they agree.
- Work out what the string looks like after each step of the odd one out. Write
  the intermediate values down rather than reasoning about it in your head. Trace of the odd one: " The HANGOVER " → title → " The Hangover " → strip → "The Hangover" → lower → "the hangover"
- In the second block, `.strip()` is applied to each name after splitting rather
  than to the whole string before. What would go wrong if you stripped first and
  split second? If you stripped the whole string first and then split, only the spaces at the very ends would be removed. The inner spaces, like the one before alan and after GRACE, would stay attached to the individual names, so you'd get [GRACE ] and [ alan] in the output. Stripping per-part after splitting is what actually cleans each name.

## Modify

- Add `.replace(" ", "")` somewhere in the first chain. Predict where it makes a difference and where it makes none. 
  adding .replace(" ", "") before .title() (e.g. entry.strip().lower().replace(" ", "").title()) makes a difference: you get TheHangover. Adding it after .title() at the end makes the same difference. It makes no difference if placed anywhere in chains whose final result is lowercase (the third line), because the spaces get removed but .lower() output still shows them gone, actually the only place it makes no difference is nowhere here; it changes every chain's output by deleting spaces. The real point: leftmost position matters because each method works on what the previous one returned.

> Chained methods run left to right, and each one works on whatever the previous
> one handed back. Reading a chain means reading it in that order, one step at a
> time.
