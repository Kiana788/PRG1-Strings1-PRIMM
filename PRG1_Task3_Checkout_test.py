"""
Automated checks for Task 3: Applied Implementation (Discount Code Checkout).

Run with: pytest PRG1_Task3_Checkout_test.py

Place your completed PRG1_Task3_Checkout_starter.py in the same
folder as this test file before running.
"""

import importlib.util
import sys
from pathlib import Path

MODULE_PATH = Path(__file__).parent / "PRG1_Task3_Checkout_starter.py"


def load_submission():
    spec = importlib.util.spec_from_file_location("submission", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["submission"] = module
    spec.loader.exec_module(module)
    return module


submission = load_submission()


# ---- functions that already worked before you started: a quick regression check ----

def test_existing_functions_still_work():
    assert submission.format_price(12.5) == "£12.50"
    assert submission.calculate_subtotal(8.00, 8) == 64.0
    assert submission.apply_standard_discount(64.0) == 57.6
    assert submission.apply_standard_discount(4.0) == 4.0


# ---- validate_discount_code ----

def test_validate_discount_code_accepts_a_valid_code():
    assert submission.validate_discount_code("SAVEIT") is True


def test_validate_discount_code_rejects_lowercase():
    assert submission.validate_discount_code("saveit") is False


def test_validate_discount_code_rejects_wrong_length():
    assert submission.validate_discount_code("SAVEMONEY") is False
    assert submission.validate_discount_code("SAVE") is False


def test_validate_discount_code_rejects_non_letters():
    assert submission.validate_discount_code("SAVE1X") is False


def test_validate_discount_code_rejects_empty_string():
    assert submission.validate_discount_code("") is False


# ---- apply_discount_code ----

def test_apply_discount_code_applies_20_percent_for_a_valid_code():
    assert submission.apply_discount_code(64.0, "SAVEIT") == 51.2


def test_apply_discount_code_applies_code_discount_below_standard_threshold_too():
    # Unlike the standard discount, a valid code should apply even to small orders.
    assert submission.apply_discount_code(4.0, "SAVEIT") == 3.2


def test_apply_discount_code_falls_back_to_standard_discount_for_invalid_code():
    assert submission.apply_discount_code(64.0, "invalid") == 57.6


def test_apply_discount_code_falls_back_and_gives_no_discount_below_threshold():
    assert submission.apply_discount_code(4.0, "invalid") == 4.0


def test_apply_discount_code_falls_back_for_empty_code():
    assert submission.apply_discount_code(64.0, "") == 57.6


# ---- print_order_summary: must be extended to accept a discount code ----

def test_print_order_summary_still_works_without_a_code():
    total = submission.print_order_summary("Notebook", 8.00, 8)
    assert total == 57.6


def test_print_order_summary_applies_a_valid_discount_code():
    total = submission.print_order_summary("Notebook", 8.00, 8, "SAVEIT")
    assert total == 51.2


def test_print_order_summary_ignores_an_invalid_discount_code():
    total = submission.print_order_summary("Notebook", 8.00, 8, "invalid")
    assert total == 57.6


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
