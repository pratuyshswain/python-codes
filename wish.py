# 24-Hour Clock	12-Hour Clock	Period
# 00:00	12:00 AM	Midnight
# 01:00	1:00 AM	    Morning
# 11:00	11:00 AM	Morning
# 12:00	12:00 PM	Noon
# 13:00	1:00 PM	    Afternoon

# 16:00	4:00 PM	    Afternoon
# 17:00	5:00 PM	    Afternoon/Evening
# 18:00	6:00 PM	    Evening

# 20:00	8:00 PM	    Evening
# 21:00	9:00 PM	    Night

# 23:00	11:00 PM	Night
import time

# Get only the hour as an integer
hour = int(time.strftime("%H"))
if hour < 12:
    print("Good Morning")
elif hour < 16:
    print("Good Afternoon")
elif hour < 20:
    print("Good Evening")
else:
    print("Good Night")
