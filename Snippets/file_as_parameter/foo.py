import sys

print(sys.argv)

with open(sys.argv[1], 'r') as file:
    for line in file:
        print(line)