# Stretch 2: Building a string

File: `building.py`

Optional. Only if you have finished the four core activities.

Two programs that construct a new string rather than picking one apart.

## Predict

- What does `initials_of("ada byron lovelace")` return?
- What does `initials_of("Grace Hopper")` return?
- What does the redaction line print?
A.B.L.
G.H.
The code is ******** until Friday


## Run

Execute and compare.

## Investigate

- `initials` starts as `""`. Why not `" "` or `"."`? This is the same question
  as an accumulator starting at 0 rather than 1, which you met with loops. 
  Starting with "" matters because the first concatenation must add nothing extra: "" + "A." is "A.". Starting with " " or "." would give " A.B.L." or ".A.B.L.". Same as an accumulator starting at 0, the neutral element for the operation.

- Trace `initials_of("Grace Hopper")` by hand: write down what `initials` holds
  after each pass.
  Trace for "Grace Hopper": pass 1 initials = "G.", pass 2 initials = "G.H.", return "G.H.".

- `"*" * len(secret)` produces a run of stars. What does the `*` operator do
  when one side is a string and the other is a number?
  string * number repeats the string that many times; "*" * 7 is "*******".

- `redact` uses `.replace`, which replaces **every** occurrence. When would that
  be exactly what you want, and when would it be a fault?
  .replace replacing every occurrence is what you want when every occurrence should go (redacting a word everywhere). It's a fault when only one spot should change, e.g. replacing a person's name would also mangle it if it appears inside another word.

## Modify

- Make `initials_of` skip any word shorter than two characters, so a stray
  initial in the input does not produce a doubled full stop.
- Make `redact` leave the last four characters visible, the way a bank does with
  a card number.
  def initials_of(full_name):
    initials = ""
    for part in full_name.split(" "):
        if len(part) &lt; 2:
            continue
        initials = initials + part[0].upper() + "."
    return initials


def redact(text, secret):
    stars = "*" * (len(secret) - 4) + secret[-4:]
    return text.replace(secret, stars)

redact("The code is SAVE2024 until Friday", "SAVE2024") now prints The code is ****2024 until Friday.


> Building a string across a loop is the same accumulator pattern you met on
> Day 3, with a different starting value and a different operator.
