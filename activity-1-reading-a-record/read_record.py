record = "Lovelace,Ada,1815,mathematician"

parts = record.split(",")

surname = parts[0]
forename = parts[1]
born = parts[2]
role = parts[3]

print(f"{forename} {surname} was born in {born} and worked as a {role}.")
print(f"Initials: {forename[0]}.{surname[0]}.")

record = "Lovelace,Ada,1815,mathematician,England"
parts = record.split(",")
surname, forename, born, role, country = parts[0], parts[1], parts[2], parts[3], parts[4]
print(f"{forename} {surname} was born in {born} and worked as a {role} in {country}.")
