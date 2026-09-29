# Activity 3: Checking a discount code

File: `check_discount_code.py`

A shop accepts discount codes. A valid one is exactly eight characters, starts
with `SAVE`, and ends with four digits. Five codes are tried.

This is the closest activity to Task 3, which you get this afternoon. Pay
attention to how the checks are ordered and how the input is handled before any
check happens at all.

## Predict

Five codes. For each, write down accepted or rejected, and your reason:

- `save2024`
- ` SAVE1234 `
- `SAVE12`
- `SALE1234`
- `SAVE12AB`

## Run

Execute and compare. Two of the five surprise most people.

## Investigate

- `save2024` is lowercase, and it is accepted. Which line made that possible?
- ` SAVE1234 ` has spaces at both ends and is still accepted. Same question.
- `is_valid` reassigns `code` on its first line. What would happen if it checked
  the original `code` instead? Try it.
- The three checks return `False` as soon as one fails, rather than working out
  all three and combining them. What does that buy you?
- `code[4:]` takes everything from position 4 onwards. Why 4? What would you
  have to change if the prefix became `DISCOUNT`?

## Modify

- The shop wants codes to be ten characters with six digits. Make that change.
  How many numbers did you have to touch, and could the code have been written
  so it was fewer?
- Add a rule: codes beginning `SAVE00` are expired and must be rejected, even
  though they otherwise look valid. Where does that check have to go?

> Notice what the program does before it checks anything: it normalises. A
> discount code a customer types will have the wrong case and stray spaces, and
> a checker that does not allow for that will reject perfectly good codes.
