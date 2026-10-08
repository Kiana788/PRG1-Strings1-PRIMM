def initials_of(full_name):
    initials = ""
    for part in full_name.split(" "):
        if len(part) in (0, 1):
            continue
        initials = initials + part[0].upper() + "."
    return initials

def redact(text, secret):
    stars = "*" * (len(secret) - 4) + secret[-4:]
    return text.replace(secret, stars)


print(initials_of("ada byron lovelace"))
print(initials_of("Grace Hopper"))

print(redact("The code is SAVE2024 until Friday", "SAVE2024"))
