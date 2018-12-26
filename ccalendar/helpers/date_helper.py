
from datetime import date
from datetime import datetime
from dateutil.parser import parse
import time

def combine_date(x):
    to_time = None
    if x.get("start").get("dateTime") is not None and parse(x.get("start").get("dateTime")).replace(
                                                                                                tzinfo=None) > datetime.utcnow():
        to_time = parse(x.get("start").get("dateTime")).timetuple()

    elif x.get("start").get("date") is not None:
        combined = parse(x.get("start").get("date"))
        combined = datetime.combine(combined, datetime.min.time()).timetuple()

        to_time = combined
    else:
        return 0
    return time.mktime(to_time)