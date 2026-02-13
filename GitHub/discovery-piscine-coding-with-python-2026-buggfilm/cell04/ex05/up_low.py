result = ""

text = input()

for c in text:
    if c.islower():
        result += c.upper()
    elif c.isupper():
        result += c.lower()
    else:
        result += c

print(result)
