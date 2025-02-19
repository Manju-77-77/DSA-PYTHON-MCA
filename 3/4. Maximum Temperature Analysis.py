def temperature_analysis(temps):
    cities = len(temps)
    days = len(temps[0])

    highest_temp = [0] * cities
    highest_day = [0] * cities
    avg_temp = [0] * cities

    for i in range(cities):
        max_temp = temps[i][0]
        max_day = 0
        total = 0
        for j in range(days):
            if temps[i][j] > max_temp:
                max_temp = temps[i][j]
                max_day = j
            total += temps[i][j]
        
        highest_temp[i] = max_temp
        highest_day[i] = max_day
        avg_temp[i] = total // days 

    return highest_temp, highest_day, avg_temp

# Example
temps = [
    [30, 32, 35, 40, 38],
    [28, 31, 34, 36, 37],
    [25, 27, 30, 32, 33]
]

high_temp, high_day, avg_temp = temperature_analysis(temps)
print("Highest Temperatures:", high_temp)
print("Days of Highest Temperatures:", high_day)
print("Average Temperatures:", avg_temp)
