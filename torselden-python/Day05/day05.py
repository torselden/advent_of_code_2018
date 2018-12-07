import os
import sys
import re
from datetime import datetime

def parse_input(file):  
    with open(os.path.join(sys.path[0], file ), 'rU') as input_file:
        # return map(chars.extend, input_file)
        return input_file.readline()
    

def react(input):    
    pos = 1
    data = list(input)

    while pos < len(data)-1:
        try:
            while abs(ord(data[pos]) - ord(data[pos-1])) == 32:
                del data[pos-1]
                del data[pos-1]
                pos -= 1
            pos +=1
        except:
            break

    result = len(data)
    return result,data

def day_5a():
    input = parse_input('5.txt') 
    result,_ = react(input)
    return result

def remove_and_react(output):
    min_length = len(output)

    for i in range(ord('a'),ord('z')+1):
        # data = [x for x in output if (x != chr(i) and x != chr(i-32))]
        data = [x for x in output if x not in [chr(i),chr(i-32)]]
        result,_ = react(data)
        if result<min_length:
            min_length = result
    
    return min_length

def day_5b():
    input = parse_input('5.txt') 
    return remove_and_react(input)

print(day_5a())
print(day_5b())
