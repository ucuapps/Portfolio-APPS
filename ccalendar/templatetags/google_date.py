from django import template
from dateutil.parser import parse
from  datetime import datetime


register = template.Library()


@register.filter(name='to_day')
def to_day(value):
    weekDays = [None]*7
    weekDays[0] = "Пн"
    weekDays[1] = "Вт"
    weekDays[2] = "Ср"
    weekDays[3] = "Чт"
    weekDays[4] = "Пт"
    weekDays[5] = "Сб"
    weekDays[6] = "Нд"
    if value.get("dateTime") is not None:
        date = parse(value)
        return weekDays[date.weekday()]
    elif value.get("date") is not None:
        combined = datetime.combine(parse(value.get("date")), datetime.min.time())
        return weekDays[combined.weekday()]
    else:
        return ""


@register.filter(name='to_month_day')
def to_month_day(value):
    if value.get("dateTime") is not None:
        date = parse(value)
        return str(date.day)
    elif value.get("date") is not None:
        date = datetime.combine(parse(value.get("date")), datetime.min.time())
        return str(date.day)
    else:
        return ""


@register.filter(name='to_month')
def to_month(value):

    month = [None] * 12
    month[0] = "січ"
    month[1] = "лют"
    month[2] = "бер"
    month[3] = "кві"
    month[4] = "тра"
    month[5] = "чер"
    month[6] = "лип"
    month[7] = "сер"
    month[8] = "вер"
    month[9] = "жов"
    month[10] = "лис"
    month[11] = "гру"
    if value.get("dateTime") is not None:
        date = parse(value)
        return month[date.month-1]
    elif value.get("date") is not None:
        date = datetime.combine(parse(value.get("date")), datetime.min.time())
        return month[date.month-1]
    else:
        return ""


@register.filter(name='to_month_num')
def to_month_num(value):
    if value.get("dateTime") is not None:
        date = parse(value)
        return date.month-1
    elif value.get("date") is not None:
        date = datetime.combine(parse(value.get("date")), datetime.min.time())
        return date.month-1
    else:
        return ""


@register.filter(name='to_hour')
def to_hour(value):
    if value.get("dateTime") is not None:
        date = parse(value)
        if date.hour<10:
            return "0"+str(date.hour)
        return date.hour
    elif value.get("date") is not None:
        date = datetime.combine(parse(value.get("date")), datetime.min.time())
        if date.hour<10:
            return "0"+str(date.hour)
        return date.hour
    else:
        return ""


@register.filter(name='to_minute')
def to_minute(value):
    if value.get("dateTime") is not None:
        date = parse(value)
        if date.minute == 0:
            return "00"
        elif date.minute <10:
            return "0"+str(date.minute)
        return date.minute
    elif value.get("date") is not None:
        date = datetime.combine(parse(value.get("date")), datetime.min.time())
        if date.minute == 0:
            return "00"
        elif date.minute <10:
            return "0"+str(date.minute)
        return date.minute
    else:
        return ""


@register.filter(name='location')
def location(value):
    value= value.split(" ")[0]
    return value


@register.filter(name='color_filter')
def color_filter(value):
    variants = {
        'confirmed': '#4CAF50',
        'tentative': '#FFEB3B',
        'cancelled': '#f44336',
    }
    return variants.get(value)


@register.filter(name='status_filter')
def color_filter(value):
    variants = {
        'confirmed': 'event_confirmed',
        'tentative': 'event_waiting',
        'cancelled': 'event_canceled',
    }
    return variants.get(value)