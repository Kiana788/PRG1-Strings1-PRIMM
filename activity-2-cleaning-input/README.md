# Activity 2: Cleaning what people typed

File: `clean_signups.py`

Five people signed up. Some of them are the same person. The program works out
how many are actually distinct.

## Predict

- How many entries are accepted? 3 
- Which ones are rejected, and why? 
Accepted: alice@example.com Rejected, already signed up: alice@example.com
Accepted: bob@example.com
Rejected, already signed up: bob@example.com
Accepted: carol@example.com

- What does the final line say? 
3 unique sign-ups from 5 entries.

## Run

Execute and compare.

## Investigate

- Look at the five raw entries. To a human, how many different people are there?
  The program agrees. What did it have to do first to get there?
  There are 3 different people. The program had to normalise (clean) every entry first, because " Alice@Example.com " and "alice@example.com" are only the same after cleaning.

- `clean` does two things in one line. Name both, and say what each one removes.
clean does two things: .strip() removes whitespace from both ends; .lower() removes case differences by mapping everything to lowercase.

- Delete `.strip()` from `clean` and predict the new output before running it.
  Then delete `.lower()` instead. Which one mattered more, and why?
   the padded entries no longer match, so output becomes 5 accepted, 0 rejected. Delete .lower(): alice@example.com still matches its lowercase twin, but "Alice@Example.com" and "BOB@example.com" become "new" people, so 5 accepted again. On this data both matter equally (2 extra acceptances each); on real data case is usually the bigger issue for emails.

- The check is `if cleaned in accepted:`. What would happen if it compared the
  raw `entry` instead?
the whitespace and case would never match, so duplicates slip through and all 5 get accepted. The de-dup would be broken.

## Modify

- Someone signs up as `ALICE@EXAMPLE.COM`. Confirm the program already handles
  it, and say which line does the work.
  ALICE@EXAMPLE.COM is already handled by the line cleaned = clean(entry) (specifically the .upper()... rather, .lower() inside clean) before the if check ever sees it.

- A trailing full stop gets typed by accident: `alice@example.com.`. The program
  treats that as a new person. Should it? Decide with your partner before you
  change anything.
  alice@example.com. is genuinely a different string, so the program treating it as a new person is technically consistent, but as a design decision it's a fault, it's clearly the same person. You could add .rstrip(".") to clean, but decide with your partner whether a real address could legitimately end in a dot (it can't) before changing it.
> Normalising input before comparing it is one of the most common jobs in real
> software, and forgetting to do it is one of the most common faults. You will
> need this again in about an hour.
