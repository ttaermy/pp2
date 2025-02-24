#1
import re
pattern = r"ab*"

st = input()

if re.fullmatch(pattern, st):
    print(f"Match: {st}")
else:
    print(f"No match: {st}")


#2
import re
pattern = r"ab{2,3}"

st = input ()

if re.fullmatch(pattern, st):
    print(f"Match")
else:
    print(f"No Match")


#3
import re
pattern = r"[a-z]+_[a-z]+"

st = input()

if re.fullmatch(pattern, st):
    print(f"Match")
else:
    print(f"No match")

#4
import re
pattern = r"[A-Z][a-z]+"

st = input()

if re.fullmatch(pattern, st):
    print(f"Match")
else:
    print(f"No match")

#5
import re
pattern = r"a.*b"

st = input()

if re.fullmatch(pattern, st):
    print(f"Match")
else:
    print(f"No match")


#6
import re
pattern = r"[ ,.]"
st = input()

x = re.sub(pattern, ":", st)
print(x)


#7
import re
pattern = r"_(.)"
st = input()

def convert(match):
    return match.group(1).upper()

x = re.sub(pattern, convert, st)
print(x)

#8
import re

st = input()
x = re.split(r"[^A-Z]+", st)
print(x)

#9
import re

st = input()

def add_space(match):
    return " " + match.group(1)

pattern = r"(?<!^)([A-Z])"
x = re.sub(pattern, add_space, st)

print(x)


#10
import re
pattern = r"(?<!^)([A-Z])"
st = input()

def convert(match):
    return "_" + match.group(1).lower()

x = re.sub(pattern, convert, st)
print(x.lower())