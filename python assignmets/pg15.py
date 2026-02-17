s = "thequickbrownfoxjumpsoverthelazydog"
for ch in set(s):
    if s.count(ch) > 1:
        print(ch, ":", s.count(ch))
