import re

a = "https github.com rajatchauhan git/python-for-devops, git"
# pattern = r"/"

# b = re.split(pattern, a)
# print(b)

pattern = r"git"

b = re.search(pattern, a)
if b:
    print("pattern found", b.group())
else:
    print("pattern not found")

# pattern = r"github.com"
# b = re.match(pattern, a)
# if b:
#     print("match found", b.group())
# else:
#     print("match not found")

