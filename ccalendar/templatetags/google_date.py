from django import template
from dateutil.parser import parse
import datetime


register = template.Library()


@register.filter(name='to_day')
def to_day(value):
    date = parse(value)
    weekDays = [None]*7
    weekDays[0] = "Пн"
    weekDays[1] = "Вт"
    weekDays[2] = "Ср"
    weekDays[3] = "Чт"
    weekDays[4] = "Пт"
    weekDays[5] = "Сб"
    weekDays[6] = "Нд"
    return weekDays[date.weekday()]


@register.filter(name='to_month_day')
def to_month_day(value):
    date = parse(value)
    return str(date.day)


@register.filter(name='to_month')
def to_month(value):
    date = parse(value)
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
    return month[date.month-1]

@register.filter(name='to_month_num')
def to_month_num(value):
    date = parse(value)
    return  date.month-1



@register.filter(name='to_hour')
def to_hour(value):
    date = parse(value)
    if date.hour< 10:
        return "0"+str(date.hour)
    return date.hour


@register.filter(name='to_minute')
def to_minute(value):
    date = parse(value)
    if date.minute == 0:
        return "00"
    elif date.minute <10:
        return "0"+str(date.minute)
    return date.minute


@register.filter(name='location')
def location(value):
    value= value.split(" ")[0]
    return value


@register.filter(name='color_filter')
def color_filter(value):
    variants = {
        'needsAction': '#FFEB3B',
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
        'needsAction': 'event_waiting',
        'cancelled': 'event_canceled',
    }
    return variants.get(value)