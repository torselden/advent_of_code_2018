import os
import sys
import re

def parse_input(file):
    input = []
    with open(os.path.join(sys.path[0], file)) as input_file:
        for line in input_file:            
            input.append(line)

    return input

def parse(line):
    data = re.findall(r"[\d']+", line)
    return map(int,data) 

def day_3a(input):
    patches = {}
    for line in input:
        id, x,y,w,h = parse(line)
        for i in range(x,x+w):
            for j in range(y,y+h):
                d = str(i)+':'+str(j)
                if d in patches.keys():
                    patches[d] += 1
                else:
                    patches[d] = 1
    return len(list(v for k,v in patches.items() if v>1))

def day_3b(input):
    patches = {}
    for line in input:
        id, x,y,w,h = parse(line)
        for i in range(x,x+w):
            for j in range(y,y+h):
                d = str(i)+':'+str(j)
                if d in patches.keys():
                    patches[d] +=   1
                else:
                    patches[d] = 1

    for line in input:
        id,x,y,w,h = parse(line)
        ans = True
        # k = [key for key in patches.items() if id in key]
        # g = (key for key in patches.items() if id in key)

        for i in range(x,x+w):
            for j in range(y,y+h):
                d = str(i)+':'+str(j)
                if patches[d] > 1:
                    ans = False
                    break

        if ans == True:
            print(id)



# print(day_3a(parse_input('3.txt')))
print(day_3b(parse_input('3.txt')))
