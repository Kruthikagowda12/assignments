s = "HikRuthIka "
count = 0
for c in s[:4]:
    if c.isupper():
        count += 1
if count >= 2:
    print(s.upper())
else:
    print(s)

