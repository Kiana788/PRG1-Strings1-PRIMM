# Activity 1: Reading a record

File: `read_record.py`

One line of comma-separated data, of the kind that comes out of a spreadsheet
export or a database dump, turned into something a person can read.

## Predict

Write down both lines of output before running anything.
>Ada Lovelace was born in 1815 and worked as a mathematician. Initials: A.L.

## Run

Execute it.

## Investigate

- `record.split(",")` produced something with four pieces in it. What type is
  that something, and how do you know from the code alone?
A list. You can tell because the code indexes it with integer positions in square brackets (parts[0], parts[1]), which is how list items are accessed.

- `parts[0]` is the surname and `parts[1]` is the forename. Why is the surname
  at 0 rather than 1?
Python indexes from zero. The first item is at index 0, so the pieces sit at 0, 1, 2, 3.

- `forename[0]` gives a single character. What would `forename[1]` give? What
  about `forename[-1]`?
forename[1] is "d" (the second character). forename[-1] is "a" (negative indexes count from the end, so it gives the last character).

- The data has the surname first, but the output has the forename first. Which
  line does that reordering, and how much work was it?
  The first print(f"{forename} {surname} ...") line. The data never moves; the f-string just lists {forename} before {surname}. It was no work at all, since the fields were already named variables.

## Modify

- Add a fifth field to the record for the country, and include it in the output.

record = "Lovelace,Ada,1815,mathematician,England"
parts = record.split(",")
surname, forename, born, role, country = parts[0], parts[1], parts[2], parts[3], parts[4]
print(f"{forename} {surname} was born in {born} and worked as a {role} in {country}.")

Ada Lovelace was born in 1815 and worked as a mathematician in England.

- Change the separator in the data from a comma to a semicolon. What else has to
  change, and what does not?
Only the split argument changes: parts = record.split(";") (and the record itself). Nothing else changes: variable names, indexes, and print lines are untouched because the fields are positional regardless of separator.

- Remove the `role` field from the record but leave the rest of the code alone.
  Predict what happens before you run it.
record = "Lovelace,Ada,1815" leaves parts with only 3 items, but role = parts[3] still runs. Prediction: the program crashes with IndexError: list index out of range on that line, printing nothing at all, because the crash happens before any print executes.

> That last one is worth doing properly. Real data is missing fields all the
> time, and the way this program fails is exactly how a real one would.
