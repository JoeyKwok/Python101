# extract 'last 15 mins(PA alert)'

with open("Overall.csv", 'r') as f1, open("Last15mins.csv", 'w') as f2:
    for line in f1:
        time = line.split(',')
        print(time[1])
        timeframe = time[1]
        if time[1] == "last 15 mins(PA alert)":
            f2.write(line)



