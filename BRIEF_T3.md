# Task 3: Applied Implementation

Worth 15% of the module assignment | Individual work | Module code PRG1

## What you're doing

`PRG1_Task3_Checkout_starter.py` is a working checkout program for a small shop. It already calculates order totals correctly, including a standard volume discount: 10% off any order over £50. Run it now, before changing anything; it works.

The shop wants to add discount codes on top of this. Your job is to extend the program to support them, without breaking anything that currently works.

More marks are available for explaining your extension than for the code passing on its own. Working code is necessary but not sufficient here; see "Explain your approach" below before you consider this task finished.

## What's already there

These functions are complete and already correct. Read them before you start; you will call some of them, and your new code should follow the same style.

| Function | What it does |
|---|---|
| `format_price(amount)` | Returns `amount` formatted as a price string, for example `£12.50`. |
| `calculate_subtotal(unit_price, quantity)` | Returns the subtotal for `quantity` items at `unit_price` each. |
| `apply_standard_discount(subtotal)` | Applies the shop's existing discount rule: 10% off orders over £50, otherwise no discount. |
| `print_order_summary(item_name, unit_price, quantity)` | Prints a summary of the order and returns the final total. You will modify this one. |

## What you need to add

Two new functions, currently left as `pass`:

| Function | What it needs to do |
|---|---|
| `validate_discount_code(code)` | Return `True` if `code` is exactly 6 characters long and consists entirely of uppercase letters. Return `False` otherwise, including for an empty string. |
| `apply_discount_code(subtotal, code)` | If `code` is valid, apply a 20% discount to `subtotal` instead of the standard discount. If `code` is not valid (including an empty string), fall back to the shop's existing standard discount rule by calling `apply_standard_discount`. Do not re-implement that logic here; call the existing function. |

## What you need to change

`print_order_summary` currently always applies the standard discount. Modify it to accept a fourth parameter, `discount_code`, defaulting to an empty string, and use `apply_discount_code` instead of calling `apply_standard_discount` directly. Existing calls to `print_order_summary` with no discount code should carry on working exactly as they do now.

## Check your own work

`PRG1_Task3_Checkout_test.py` is provided. With both files in the same folder, run:

`pytest PRG1_Task3_Checkout_test.py -v`

A few tests pass immediately, before you change anything: these confirm the existing functions still work and that `print_order_summary` is not broken. The rest will fail until you have completed the extension.

## A note on approach

You do not need lists, dictionaries, or anything beyond what has been covered up to and including strings. `validate_discount_code` needs string checks only; you do not need to loop through the code character by character.

## Explain your approach

This section carries more of the marks for this task than the code itself. Passing tests shows your code works; these questions show you understand why. Answer in `ANSWERS_T3.md`, in your own words, specific to this program, not as a general description of how functions or discounts work.

1. Explain why `apply_discount_code` calls `apply_standard_discount` instead of repeating its 10%-over-£50 logic. What would you lose if you duplicated that logic instead of calling the existing function?
2. Without running it, work out what `print_order_summary("Pen", 2.00, 2, "invalid")` prints. Walk through it line by line: what is the subtotal, what does `apply_discount_code` do with an invalid code, and what is the final total?
3. `print_order_summary` now has a fourth parameter, `discount_code`, with a default value of an empty string. Explain why the default value matters here. What would break, and for whom, if you had made it a required parameter instead?
4. `validate_discount_code` checks `code.isalpha()` rather than `code.isalnum()`. Explain what `isalnum()` additionally allows that `isalpha()` does not, and give a specific 6-character code containing at least one digit that would be wrongly accepted as valid if `isalpha()` were replaced with `isalnum()`.

## If you used an AI tool

AI tool use on this task does not need to be logged separately. At the end of the module you will complete one short reflection, `PRG1_AI_Use_Reflection`, covering AI use across the whole assignment. It is mandatory to submit, but not marked.

## Submission

Submit your completed `PRG1_Task3_Checkout_starter.py` file, alongside `ANSWERS_T3.md` with the four questions above answered.
