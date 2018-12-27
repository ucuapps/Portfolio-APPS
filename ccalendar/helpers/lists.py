
from google.oauth2 import service_account
from dateutil.parser import parse
from googleapiclient.errors import HttpError
from ccalendar import config
from datetime import datetime

import googleapiclient.discovery
import time
import sys
import json


def calendar_list(buildingId):

    with open('/home/main/home/buildings.json') as f:
        calendars = json.load(f)
    if datetime.datetime.today().day - datetime.datetime.fromisoformat(calendars.get("date")).day == 0:
        return filter(lambda x: x.get("buildingId") == buildingId,calendars.get("items"))

    SCOPES = ['https://www.googleapis.com/auth/admin.directory.resource.calendar']
    SERVICE_ACCOUNT_FILE = config.google_path

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    # credentials.create_delegated("zavaliy@ucu.edu.ua")
    credentials = credentials.with_subject('zavaliy@ucu.edu.ua')
    resourceApi = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

    result = resourceApi.resources().calendars().list(customer="C01ak6gy3",
                                                      ).execute()

    with open('/home/main/home/buildings.json', 'w') as fp:

        json.dump({'items':result.get("items"), 'date': datetime.datetime.today().isoformat()}, fp)

        return filter(lambda x: x.get("buildingId") == buildingId,result.get("items"))


def room_calendar(buildingId, roomId):
    rooms = calendar_list(buildingId)
    result = filter(lambda x: int(x["resourceId"]) == int(roomId), rooms)

    # result = filter(lambda x: x.get("buildingId") == buildingId, result.get("items"))
    return result


def load_more(building_id, load_date, room_id=False, before=False):
    calendars = calendar_list(building_id)

    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = config.google_path

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    calendar_api = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    if room_id is not False:
        calendars = filter(lambda x: int(x["resourceId"]) == int(room_id), calendars)

    events = {}
    if before is False:
        max_day = parse(load_date) + datetime.timedelta(days=1)
        max_day = max_day.isoformat()
        load_dt = parse(load_date).replace(tzinfo=None)
        count = 0
        for calendar in calendars:
            try:
                if count == 0:
                    events = calendar_api.events().list(calendarId=calendar["resourceEmail"], timeMin=load_date,
                                                        singleEvents=True, timeMax=max_day,
                                                        orderBy='startTime', showDeleted=True).execute()["items"]
                    count += 1

                    continue

                events += calendar_api.events().list(calendarId=calendar["resourceEmail"], timeMin=load_date,
                                                     singleEvents=True, timeMax=max_day,
                                                     orderBy='startTime', showDeleted=True).execute()["items"]
            except(Exception):
                continue
        events = filter(lambda x: x.get("start").get("dateTime") is not None and
                                  parse(x.get("start").get("dateTime")).replace(tzinfo=None) > load_dt, events)

    elif before is True:
        min_day = parse(load_date) - datetime.timedelta(days=1)
        min_day_dt = min_day.replace(tzinfo=None)
        min_day = min_day.isoformat()
        count = 0
        load_dt = parse(load_date).replace(tzinfo=None)
        for calendar in calendars:
            try:
                if count == 0:
                    events = calendar_api.events().list(calendarId=calendar["resourceEmail"],
                                                        timeMin=min_day, timeMax=load_date,
                                                        singleEvents=True,
                                                        orderBy='startTime', showDeleted=True).execute()["items"]
                    count = 1
                    # return events
                    continue

                events += calendar_api.events().list(calendarId=calendar["resourceEmail"],
                                                     timeMin=min_day, timeMax=load_date,
                                                     singleEvents=True,
                                                     orderBy='startTime', showDeleted=True).execute()["items"]
            except(Exception):
                continue
        events = filter(lambda x: x.get("start").get("dateTime") is not None and
                                  load_dt > parse(x.get("start").get("dateTime")).replace(tzinfo=None) > min_day_dt,
                        events)

    events = sorted(events, key=lambda x: time.mktime(parse(x.get("start").get("dateTime")).timetuple()))

    return events
