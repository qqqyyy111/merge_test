def seconds_to_time(time):
    time_list = []
    for i in range(len(time)):
        seconds = i
        m, s = divmod(seconds, 60)
        if s < 10:
            time_list.append(str(m) + ":0" + str(s))
        else:
            time_list.append(str(m) + ":" + str(s))

    return time_list
