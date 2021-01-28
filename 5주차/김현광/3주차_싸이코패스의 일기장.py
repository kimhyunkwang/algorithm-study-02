string = input()
original = ""

for s in string:
    if s in ['A', 'B', 'C', 'D']:
        original += chr(ord(s) + 22)
    else:
        original += chr(ord(s) - 4)

print(original)