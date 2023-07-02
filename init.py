from astral import LocationInfo
from astral.sun import sun
from astral.planet import planet
from datetime import datetime, timedelta

def get_planetary_hour(location, date):
    city = LocationInfo(location)
    s = sun(city.observer, date=date)
    p = planet("Sun", city.observer, date=date)
    diff = (s - p).total_seconds() / 3600.0
    hour_length = 24.0 / 7.0
    day_start = datetime(date.year, date.month, date.day, 0, 0, 0)
    day_start += timedelta(hours=diff)
    current_time = datetime.now()
    time_diff = current_time - day_start
    hour_num = int(time_diff.total_seconds() / 3600.0 / hour_length)
    return hour_num

location = "Oakland"
date = datetime.now()
hour_num = get_planetary_hour(location, date)
print(f"Current planetary hour for {location} is {hour_num}")


    