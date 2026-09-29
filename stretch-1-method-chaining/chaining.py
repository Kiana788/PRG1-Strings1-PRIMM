entry = "  The HANGOVER  "

print(entry.strip().lower().title())
print(entry.lower().strip().title())
print(entry.title().strip().lower())

print("---")

messy = "  ada,GRACE ,  alan  "

for name in messy.split(","):
    print(f"[{name.strip().capitalize()}]")
