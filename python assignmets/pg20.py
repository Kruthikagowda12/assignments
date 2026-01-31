s = "aaaabbbbccddee"

a = s[0]

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        a += s[i]

print(a)
