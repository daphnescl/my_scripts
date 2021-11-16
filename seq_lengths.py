import sys
with open(sys.argv[l], "r") as fh:
    lines = fh.readlines()

for line in lines:
    print(len(line))
