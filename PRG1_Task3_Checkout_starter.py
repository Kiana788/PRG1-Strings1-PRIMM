"""
Discount Code Checkout

Calculates order totals for a small shop, including a standard
volume discount. This program already works: run it, and it prints
a correct order summary using the standard discount rule.

Three things need changing: the two functions marked below as not
yet implemented, and print_order_summary. See the task brief for 
the detail of each.

Your job is to extend it to support discount codes, without breaking
the parts that already work.
"""

CURRENCY_SYMBOL = "£"
STANDARD_DISCOUNT_THRESHOLD = 50
STANDARD_DISCOUNT_RATE = 0.10
CODE_DISCOUNT_RATE = 0.20


def format_price(amount):
    """Return amount formatted as a price string, for example £12.50."""
    return f"{CURRENCY_SYMBOL}{amount:.2f}"


def calculate_subtotal(unit_price, quantity):
    """Return the subtotal for quantity items at unit_price each."""
    return unit_price * quantity


def apply_standard_discount(subtotal):
    """Apply the standard discount: 10% off orders over £50, otherwise no discount."""
    if subtotal > STANDARD_DISCOUNT_THRESHOLD:
        return subtotal * (1 - STANDARD_DISCOUNT_RATE)
    return subtotal


def validate_discount_code(code):
    """Return True if code is a valid discount code: exactly 6 characters,
    all uppercase letters. Not yet implemented.
    """
    pass


def apply_discount_code(subtotal, code):
    """If code is a valid discount code, apply a 20% discount instead of
    the standard discount. Otherwise, fall back to the standard discount
    by calling apply_standard_discount. Not yet implemented.
    """
    pass


def print_order_summary(item_name, unit_price, quantity):
    """Print a summary of the order and return the final total.

    Needs changing. It must take a fourth parameter, discount_code, 
    defaulting to an empty string, and use apply_discount_code 
    rather than calling apply_standard_discount directly. Existing 
    calls that pass only three arguments must keep working.
    """
    subtotal = calculate_subtotal(unit_price, quantity)
    total = apply_standard_discount(subtotal)
    print(f"{quantity} x {item_name} @ {format_price(unit_price)}")
    print(f"Subtotal: {format_price(subtotal)}")
    print(f"Total: {format_price(total)}")
    return total


if __name__ == "__main__":
    print_order_summary("Notebook", 8.00, 8)


def validate_discount_code(code):
    """Return True if code is a valid discount code: exactly 6 characters,
    all uppercase letters.
    """
    return len(code) == 6 and code.isalpha() and code == code.upper()


def apply_discount_code(subtotal, code):
    """If code is a valid discount code, apply a 20% discount instead of
    the standard discount. Otherwise, fall back to the standard discount
    by calling apply_standard_discount.
    """
    if validate_discount_code(code):
        return subtotal * (1 - CODE_DISCOUNT_RATE)
    return apply_standard_discount(subtotal)


def print_order_summary(item_name, unit_price, quantity, discount_code=""):
    """Print a summary of the order and return the final total."""
    subtotal = calculate_subtotal(unit_price, quantity)
    total = apply_discount_code(subtotal, discount_code)
    print(f"{quantity} x {item_name} @ {format_price(unit_price)}")
    print(f"Subtotal: {format_price(subtotal)}")
    print(f"Total: {format_price(total)}")
    return total
