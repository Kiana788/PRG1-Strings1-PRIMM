def clean(entry):
    return entry.strip().lower()


signups = [
    "  Alice@Example.com ",
    "alice@example.com",
    "BOB@example.com  ",
    "bob@Example.com",
    "carol@example.com",
]

accepted = []

for entry in signups:
    cleaned = clean(entry)
    if cleaned in accepted:
        print(f"Rejected, already signed up: {cleaned}")
    else:
        accepted.append(cleaned)
        print(f"Accepted: {cleaned}")

print(f"{len(accepted)} unique sign-ups from {len(signups)} entries.")
