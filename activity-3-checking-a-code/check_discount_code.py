VALID_PREFIX = "SAVE"
CODE_LENGTH = 8


def normalise(code):
    return code.strip().upper()


def is_valid(code):
    code = normalise(code)

    if len(code) != CODE_LENGTH:
        return False
    if not code.startswith(VALID_PREFIX):
        return False
    if not code[4:].isdigit():
        return False
    if code.startswith("SAVE00"):
        return False

    return True


entered_codes = ["save2024", " SAVE1234 ", "SAVE12", "SALE1234", "SAVE12AB"]

for entry in entered_codes:
    if is_valid(entry):
        print(f"{entry} accepted, discount applied")
    else:
        print(f"{entry} rejected")
