# Activity 2: Cleaning what people typed

File: `clean_signups.py`

Five people signed up. Some of them are the same person. The program works out
how many are actually distinct.

## Predict

- How many entries are accepted?
- Which ones are rejected, and why?
- What does the final line say?

## Run

Execute and compare.

## Investigate

- Look at the five raw entries. To a human, how many different people are there?
  The program agrees. What did it have to do first to get there?
- `clean` does two things in one line. Name both, and say what each one removes.
- Delete `.strip()` from `clean` and predict the new output before running it.
  Then delete `.lower()` instead. Which one mattered more, and why?
- The check is `if cleaned in accepted:`. What would happen if it compared the
  raw `entry` instead?

## Modify

- Someone signs up as `ALICE@EXAMPLE.COM`. Confirm the program already handles
  it, and say which line does the work.
- A trailing full stop gets typed by accident: `alice@example.com.`. The program
  treats that as a new person. Should it? Decide with your partner before you
  change anything.

> Normalising input before comparing it is one of the most common jobs in real
> software, and forgetting to do it is one of the most common faults. You will
> need this again in about an hour.
