# Task 3: Applied Implementation, Marking Scheme

Companion to `BRIEF_T3.md` | Module code PRG1

20 marks total, 15% of the module assignment: 8 for code correctness, 12 for explaining your approach across 4 questions.

## Part 1: Code correctness, 8 marks

Run `pytest PRG1_Task3_Checkout_test.py -v` against the submission.

| Group | Marks | Covers |
|---|---|---|
| Existing functions unaffected | 1 | `test_existing_functions_still_work`. |
| `validate_discount_code` | 2 | The 5 `validate_discount_code` tests. |
| `apply_discount_code` | 2 | The 5 `apply_discount_code` tests; fallback must call `apply_standard_discount`, not re-implement it. |
| `print_order_summary` extended | 2 | The 3 `print_order_summary` tests, including the no-code case still working unchanged. |
| Code quality | 1 | Matches existing style; genuinely reuses `apply_standard_discount` and `validate_discount_code`. |

## Part 2: Explain your approach, 12 marks

| Marks | What it shows |
|---|---|
| 9-12 | All four answers correct, specific to this program, clearly reasoned. |
| 5-8 | Some answers correct and specific; others incomplete or generic. |
| 0-4 | Mostly incorrect, generic, or restates the code without addressing why. |
