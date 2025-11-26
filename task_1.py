time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
time_str = time_str.replace(' ', ',')

time_list = time_str.split(',')

total_minutes = 0

for time in time_list:
    if 'h' in time:
        h = int(time[:-1])
        total_minutes += h * 60
    elif 'm' in time:
        m = int(time[:-1])
        total_minutes += m
    elif 's' in time:
        s = int(time[:-1])
        total_minutes += s // 60

print(total_minutes) 