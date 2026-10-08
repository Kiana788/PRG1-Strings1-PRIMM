# Activity 3: Checking a discount code

File: `check_discount_code.py`

A shop accepts discount codes. A valid one is exactly eight characters, starts
with `SAVE`, and ends with four digits. Five codes are tried.

This is the closest activity to Task 3, which you get this afternoon. Pay
attention to how the checks are ordered and how the input is handled before any
check happens at all.

## Predict

Five codes. For each, write down accepted or rejected, and your reason:
  code        result.     reason 
- `save2024` accepted	    normalise uppercases it
- ` SAVE1234` accepted	  normalise strips the spaces
- `SAVE12`.   rejected	  only 6 characters, needs 8
- `SALE1234`. rejected	  doesn't start with SAVE
- `SAVE12AB`. rejected	  last four characters aren't all digits

## Run

Execute and compare. Two of the five surprise most people.

## Investigate
- save2024 is lowercase, and it is accepted. Which line made that possible?
The line return code.strip().upper() inside normalise made it possible: .upper() turns save2024 into SAVE2024 before any check runs.

- SAVE1234 has spaces at both ends and is still accepted. Same question.
The same line: the .strip() part of code.strip().upper() removes the spaces at both ends before any check runs.

- is_valid reassigns code on its first line. What would happen if it checked the original code instead? Try it.
save2024 would fail the prefix check (it starts save, not SAVE) and SAVE1234 would fail the prefix check too because of the leading space. Both "surprise" codes would be rejected instead of accepted.

- The three checks return False as soon as one fails, rather than working out all three and combining them. What does that buy you?  You stop as soon as one rule fails: the code is shorter, there are no nested if/else blocks, and you know exactly which check failed.

- code[4:] takes everything from position 4 onwards. Why 4? What would you have to change if the prefix became DISCOUNT?
4 skips over the 4-character prefix SAVE. If the prefix became DISCOUNT, you would change it to code[8:] (the length check stays the same because CODE_LENGTH is separate).


## Modify

- The shop wants codes to be ten characters with six digits. Make that change.
  How many numbers did you have to touch, and could the code have been written
  so it was fewer? 
  Change CODE_LENGTH = 10. That's the only number you touch for "ten characters with six digits" if the prefix stays SAVE (4 letters + 6 digits = 10, and code[4:] is still right). You could have written len(code) != CODE_LENGTH and code[len(VALID_PREFIX):] so the slice updates itself.

- Add a rule: codes beginning `SAVE00` are expired and must be rejected, even
  though they otherwise look valid. Where does that check have to go?     
    if code.startswith("SAVE00"):
        return False

    return True



> Notice what the program does before it checks anything: it normalises. A
> discount code a customer types will have the wrong case and stray spaces, and
> a checker that does not allow for that will reject perfectly good codes.
