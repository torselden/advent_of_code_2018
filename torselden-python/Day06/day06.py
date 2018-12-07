import os
import sys
import re
from datetime import datetime

def parse_input(file):  
    with open(os.path.join(sys.path[0], file ), 'rU') as input_file:
        return [line.strip() for line in input_file.readlines()]
    
def parse_coordinates(lines):
    return [tuple(map(int, coord.split(', '))) for coord in lines]

def calculate_finite_coords(coords):
    finite_coords = []
    for coord in coords:
        x, y = coord
        other_coords = [c for c in coords if c != coord]

        top_left = (0,0)
        bottom_left = (0,350)
        top_right = (350,0)
        bottom_right = (350,350)

        xy = False
        x_ = False
        y_ = False
        __ = False

        for other_coord in other_coords:
            x_o, y_o = other_coord

            if manhattan_dist(other_coord,top_left) < manhattan_dist(coord,top_left):
                xy = True               
            if manhattan_dist(other_coord,bottom_left) < manhattan_dist(coord,bottom_left):
                x_ = True
            if manhattan_dist(other_coord,top_right) < manhattan_dist(coord,top_right):
                y_ = True
            if manhattan_dist(other_coord,bottom_right) < manhattan_dist(coord,bottom_right):
                __ = True
                
            # if x_o > x and y_o > y:
            #     xy = True               
            # if x_o > x and y_o < y: 
            #     x_ = True
            # if x_o < x and y_o > y:
            #     y_ = True
            # if x_o < x and y_o < y:
            #     __ = True
            if xy == True and x_ == True and y_ == True and __ == True:
                finite_coords.append(coord)
                break       

    return finite_coords

def manhattan_dist(c, finite_coord):
    return (abs(c[0]-finite_coord[0]) + abs(c[1]-finite_coord[1]))

def calculate_largest_area(coords, finite_coords,size):
    result = {}

    # compare each of the finite coords with the all the rest between 0 and 351

    for x in range(1,size):
        for y in range(1,size):
            test_coord = x, y

            for finite_coord in finite_coords:
                finite_coord_is_closest = True
                dist_to_test = manhattan_dist(test_coord, finite_coord)
                for coord in [c for c in coords if c != finite_coord]:
                    if manhattan_dist(test_coord, coord) <= dist_to_test:
                        finite_coord_is_closest = False
                        break

                if finite_coord_is_closest:
                    if finite_coord in result:
                        result[finite_coord] += 1
                    else:
                        result[finite_coord] = 1

    largest_area = max(result.values()) 

    print(result)
    print(sorted(result, key=result.get))
    return largest_area

def calculate_region(coords, size):
    region_size = 0
    for x in range(1,size):
        for y in range(1,size):
            dist_sum = 0
            for coord in coords:
                dist = manhattan_dist(coord, (x,y))
                dist_sum +=dist
            if dist_sum < 10000:
                region_size += 1
    return region_size

def day_6a():
    input = parse_input('6.txt') 
    coords = parse_coordinates(input)
    finite_coords = calculate_finite_coords(coords)
    return calculate_largest_area(coords, finite_coords,351)

def day_6b():
    input = parse_input('6.txt') 
    coords = parse_coordinates(input)
    return calculate_region(coords, 350)

if __name__ == "__main__":
    print(day_6a())
    print(day_6b())
