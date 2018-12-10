import os
import sys
import re


def parse_input(file):  
    with open(os.path.join(sys.path[0], file ), 'rU') as input_file:
        return [line.strip() for line in input_file.readlines()]


def parse_instructions(input):  
    raw_instructions = [tuple(re.findall(r"\-{0,1}\d{1,5}.\s\W{0,1}\d{1,5}", line)) for line in input]
    positions = [list(map(int, c.split(','))) for c,v in raw_instructions]
    velocities = [list(map(int, v.split(','))) for c,v in raw_instructions]
    return list(zip(positions, velocities))


def time_lapse(instructions):
    minutes=0
    while(True):
        minutes +=1 
        for pos, vel in instructions:
            pos[0] += vel[0]
            pos[1] += vel[1]
        
        grid = [pos for pos, vel in instructions] 

        x_max = max(p[0] for p in grid)
        x_min = min(p[0] for p in grid)
        y_max = max(p[1] for p in grid)
        y_min = min(p[1] for p in grid)

        if (y_max - y_min) < 10:
            print_grid(grid, y_min, y_max, x_min, x_max)
            print("Number of minutes: " + str(minutes))
        
def print_grid(positions, y_min, y_max, x_min, x_max):

    l = list([pos for pos in positions])
    for i in range(y_min -1 ,y_max +1 ):
        for j in range(x_min-5, x_max+5):
           if [j,i] in l:
                print('#', end='')
           else:
                print('.', end='')
        print('\n')
   
def day_10a():
    input = parse_input('10.txt')
    instructions = parse_instructions(input)
    time_lapse(instructions)


if __name__ == "__main__":
    print(day_10a())
