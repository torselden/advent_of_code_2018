import os
import sys

def parse_input(file):
    input = []
    with open(os.path.join(sys.path[0], file)) as input_file:
        for line in input_file:            
            input.append(line)

    return input

def day_3a(input):
    pass

def day_3b(input):
    pass

print(day_3a(parse_input('3.txt')))
print(day_3b(parse_input('3.txt')))
