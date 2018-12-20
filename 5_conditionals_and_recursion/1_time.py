import time
last_epoch = time.time()

# def current_time(v):
#     hour = epoch // 60 // 60
#     since_hour =


def current_time(since_epoch):
    """Calculates current hour, minute, and second since given epoch;
    since epoch - in seconds.
    """
    hours_since = since_epoch // 60 // 60
    current_hour = hours_since - (hours_since // 24) * 24
    minutes_since = since_epoch // 60
    current_minute = minutes_since - (minutes_since // 60) * 60
    second_since = since_epoch // 1  # to round down seconds
    current_second = second_since - (second_since // 60) * 60
    a = hours_since
    b = hours_since // 24
    c = b * 24
    return current_hour, current_minute, current_second, a, b, c


# def days_since_epoch(epoch):
#     """Returns number of days since given epoch;
#     epoch - in seconds.
#     """
#     days = epoch // 60 // 60 // 24
#     return days


# print(current_time(last_epoch))
# print(days_since_epoch(last_epoch))

# 15:24:37

time_in_seconds = 15 * 60 * 60 + 24 * 60 + 37


def current_time(a):
    hours = a // 60 // 60
    minutes = (a - 60 * 60 * hours) // 60
    seconds = a - 60 * 60 * hours - 60 * minutes
    return hours, minutes, seconds


print(current_time(time_in_seconds))
