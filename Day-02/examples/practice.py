import re

a = "https github.com rajatchauhan git/python-for-devops, git"
# pattern = r"/"

# b = re.split(pattern, a)
# print(b)

# pattern = r"github"

# b = re.search(pattern, a)
# if b:
#     print("pattern found", b.group())
# else:
#     print("pattern not found")

pattern = r"github.com"
b = re.match(pattern, a)
if b:
    print("match found", b.list())
else:
    print("match not found")