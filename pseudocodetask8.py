def convert(number):
    hour = int(number/ 60)
    minute = int(number % 60)
    if hour == 1 and minute == 1:
            print(hour, 'hour', minute, 'minute')
    elif hour == 1:
        print(hour, 'hour', minute, 'minutes')
    else:
    print(hour, "hours,", minute, "minutes")
convert(71)
