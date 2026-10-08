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
current wrong outputs:
mailing list
Lovelace, .
Hopper, .
Turing, .
False


## Run

Execute it. All three are wrong.

## Investigate

- The heading is not shouted. `as_heading` clearly calls `.upper()`. Why did
  nothing happen? This one is important: what does `.upper()` actually give you
  back, and what does it do to the original?
text.upper() returns a new string and leaves text untouched; the returned value is thrown away, so as_heading returns the unchanged original. Fix: return text.upper().

- Every initial is missing. `forename[0:0]` looks like it takes the first
  character. How many characters does a slice from 0 to 0 contain?
forename[0:0] is an empty slice (0 characters, nothing from index 0 up to but not including index 0). Fix: initial = forename[0].

- The search returns `False`, but "Ada Lovelace" plainly contains "ada" as far
  as a person is concerned. What is the program comparing, and what did activity
  2 do that this does not?
search_term in full_name is case-sensitive: "ada" is not in "Ada Lovelace" as far as Python cares. Activity 2 normalised input before comparing; this doesn't. Fix: return search_term.lower() in full_name.lower().

## Fault log

| # | What you saw | What was wrong | How you fixed it |
| 1 | Heading printed in lowercase|.upper() result was discarded; strings are immutable, methods return a new one |return text.upper() |
| 2 | Lovelace, . (missing initial)|Slice [0:0] contains zero characters |initial = forename[0] |
| 3 | Search printed False|Case-sensitive comparison |Compare .lower() versions of both strings|

## Modify

Fix all three. You should get a shouted heading, `Lovelace, A.` and friends,
then `True`.
correct outputs after fixing: 
MAILING LIST
Lovelace, A.
Hopper, G.
Turing, A.
True

> Fault 1 catches nearly everyone once. A string method never changes the
> string it was called on, because strings cannot be changed at all. It hands
> you a new one, and if you do not catch it, it is gone.
