import time
from datetime import datetime
import calendar
import pytz

# Method 1: Using time.time() (This is already UTC)
epoch_seconds = int(time.time())
print(f"Method 1: {epoch_seconds}")

# Method 2: Using datetime with UTC
utc_now = datetime.now(pytz.UTC)
epoch_seconds_2 = int(utc_now.timestamp())
print(f"Method 2: {epoch_seconds_2}")

# Method 3: Using calendar and datetime
utc_now_2 = datetime.utcnow()
epoch_seconds_3 = calendar.timegm(utc_now_2.timetuple())
print(f"Method 3: {epoch_seconds_3}")
