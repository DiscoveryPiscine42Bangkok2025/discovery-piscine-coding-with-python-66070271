import sys
import re

args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    keyword, text = args
    matches = re.findall(keyword, text)
    if matches:
        print(len(matches))
    else:
        print("none")