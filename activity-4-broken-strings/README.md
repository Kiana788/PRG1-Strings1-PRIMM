# Activity 4: Broken strings

File: `mailing_list.py`

This program prepares a mailing list: a heading, then each contact as "Surname,
Initial." and finally a search check. Three things about it are wrong. Nothing
crashes.

## Predict

Work out what the output **should** be:

- A heading, shouted
- Three contacts as surname then initial, for example `Lovelace, A.`
- A search for "ada" in "Ada Lovelace"

## Run

Execute it. All three are wrong.

## Investigate

- The heading is not shouted. `as_heading` clearly calls `.upper()`. Why did
  nothing happen? This one is important: what does `.upper()` actually give you
  back, and what does it do to the original?
- Every initial is missing. `forename[0:0]` looks like it takes the first
  character. How many characters does a slice from 0 to 0 contain?
- The search returns `False`, but "Ada Lovelace" plainly contains "ada" as far
  as a person is concerned. What is the program comparing, and what did activity
  2 do that this does not?

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. You should get a shouted heading, `Lovelace, A.` and friends,
then `True`.

> Fault 1 catches nearly everyone once. A string method never changes the
> string it was called on, because strings cannot be changed at all. It hands
> you a new one, and if you do not catch it, it is gone.
