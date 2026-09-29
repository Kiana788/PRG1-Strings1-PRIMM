def initials_of(full_name):
    initials = ""
    for part in full_name.split(" "):
        initials = initials + part[0].upper() + "."
    return initials


def redact(text, secret):
    return text.replace(secret, "*" * len(secret))


print(initials_of("ada byron lovelace"))
print(initials_of("Grace Hopper"))

print(redact("The code is SAVE2024 until Friday", "SAVE2024"))
