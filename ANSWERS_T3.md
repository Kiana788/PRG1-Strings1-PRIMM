# Task 3: Applied Implementation, Answers

Complete this alongside `BRIEF_T3.md`.

## Explain your approach

### 1. Why does `apply_discount_code` call `apply_standard_discount` instead of repeating its logic?

>apply_discount_code delegates to apply_standard_discount because 10% off orders over £50 is the established rule at the shop. And if I duplicate if subtotal &gt; STANDARD_DISCOUNT_THRESHOLD: return subtotal * (1 - STANDARD_DISCOUNT_RATE) inside apply_discount_code, then there will be two different places where the same rule is implemented. In the event that the shop changes the threshold to £60 or the rate to 15%, when updating apply_standard_discount, there won't be any incentive to update the other place that implements the rule. Delegating to apply_standard_discount makes sure that the fall-back case behaves the same way as the standard rule, even for sub-£50 orders, which is what apply_discount_code(4.0, "invalid") is testing. There is just one rule that needs to be duplicated in this program, but following the same practice in a larger program causes real bugs.

### 2. Trace `print_order_summary("Pen", 2.00, 2, "invalid")`

>For print_order_summary("Pen", 2.00, 2, "invalid"), calculate_subtotal(2.00, 2) gives 4.00. Then apply_discount_code(4.0, "invalid") invokes validate_discount_code("invalid"), which fails because the string is 7 letters long, not 6. This causes apply_discount_code to use apply_standard_discount(4.0) instead. 4.00 is below £50, so there is no discount; apply_discount_code returns 4.00. The output is:
2 x Pen @ £2.00
Subtotal: £4.00
Total: £4.00
and the function returns 4.0. The important thing is that the invalid code doesn't fail or give any error messages, it simply works as if there was no code at all.


### 3. Why does the default value on `discount_code` matter?

>The default value of "" guarantees that all calls to the function work the same way: print_order_summary("Notebook", 8.00, 8) with three parameters will pass "" into discount_code, which will be rejected by validate_discount_code because of its wrong length, and as a result, the function apply_discount_code will use the standard discount, which is exactly how the previous version behaved. In case this parameter was required as a fourth one, all calls to the function from any program would raise TypeError, until some value would be provided. And the caller who does not care about the discount code must not know about this parameter at all.

### 4. `isalpha()` vs `isalnum()` in `validate_discount_code`

>isalnum() takes digits (as well as letters), while isalpha() takes only letters. Should I replace isalpha() with isalnum(), "SAVE24," which is 6 characters in total and consists of both letters and digits, will be considered an alphanumeric one and will be allowed in, while the condition in the store is that all codes consist of only letters. Thus, if the customer uses SAVE24 (the code that has the same format as in Activity 3), he or she will receive a 20% discount on something that never existed. The reason why isalpha() should be used here is that it allows only letters.