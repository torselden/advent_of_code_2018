import os
import sys
import re
from datetime import datetime

def parse_input(file):    
    input_lines = []
    with open(os.path.join(sys.path[0], file)) as input_file:
        for line in input_file:
            input_lines.append(line)
    
    return input_lines

def parse_lines(lines):
    input = []
    for line in lines:
        date_str=re.findall(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}", line)[0]
        action = line.split("] ")[1].strip()
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        v = date, action
        
        input.append(v)
    input.sort(key=lambda action: action[0])

    output = {}
    for date, action in input:
        if 'begins shift' in action:
            guard_id = int(re.findall(r"\d+",action)[0])
            continue

        if guard_id in output:            
            output[guard_id].append((date,action))
        else:
            output[guard_id] = [(date,action)]

        v = guard_id, date, action
        
    return output

def calc_sleepiest_minute(sleepiest_guard):
    sleeping = {}
    for i in range(1,len(sleepiest_guard),2):
        fall_asleep = sleepiest_guard[i-1][0].minute
        wake_up = sleepiest_guard[i][0].minute
        for min in range(fall_asleep, wake_up):
            if min in sleeping:
                sleeping[min] += 1
            else:
                sleeping[min] = 1

    sleepiest_minute = max(sleeping, key=(lambda key: sleeping[key]))
    times_sleeping = sleeping[sleepiest_minute]
    return sleepiest_minute,times_sleeping

def calculate_sleepiest_guard(data):
    guards = (g for g,d in data.items())

    sleep_times = {}
    for guard in guards:
        for i in range(1,len(data[guard]),2):
            sleep_time = data[guard][i][0].minute - data[guard][i-1][0].minute

            if guard in sleep_times: 
                sleep_times[guard] += sleep_time
            else:
                sleep_times[guard] = sleep_time
            
    sleepiest_guard = max(sleep_times, key=(lambda key: sleep_times[key]))

    return sleepiest_guard

def calculate_4b_result(output):
    
    times_asleep = 0
    sleepiest_minute = 0
    sleeping_guard = 0

    for id,guard in output.items():
        minute, times = calc_sleepiest_minute(guard)
        if times > times_asleep:
            times_asleep = times
            sleepiest_minute = minute
            sleeping_guard = id

    return sleeping_guard, sleepiest_minute

def day_4a():
    input = parse_input('4.txt')
    output = parse_lines(input)

    sleepiest_guard = calculate_sleepiest_guard(output)
    sleepiest_minute, _ = calc_sleepiest_minute(output[sleepiest_guard])
    return sleepiest_guard * sleepiest_minute

def day_4b():
    input = parse_input('4.txt')
    output = parse_lines(input)
    guard, minute = calculate_4b_result(output)

    return guard * minute    

print(day_4a())
print(day_4b())
