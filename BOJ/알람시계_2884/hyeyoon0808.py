time = list(map(int, input().split()))


if time[1] < 45: 
    if time[0] <= 0:
        print(23, 60 - (45-time[1]))
    else:
        print(time[0]-1, 60 - (45-time[1]))

else:
    print(time[0], time[1]-45)
    