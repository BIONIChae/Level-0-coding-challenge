def convert(number):
    hour = int(number/ 60)
    minute = int(number % 60)
    print(hour, "hour(s),", minute, "minute(s)")
convert(133)
