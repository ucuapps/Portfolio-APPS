from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from google.oauth2 import service_account
from dateutil.parser import parse
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import datetime
import json
import time
# from ccalendar.helpers.lists import calendar_list
import ccalendar.helpers.lists as lists
from urllib.error import URLError, HTTPError



def index(request):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/adm.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    calendarAPI = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    building = request.GET.get("building","")
    room = request.GET.get("room","")
    if building is not "" and room is not "":
        calendars = lists.room_calendar(building,room)
    elif room is "":
        calendars = lists.calendar_list(building)
    else:
        calendars = lists.calendar_list("С")
    now = datetime.datetime.utcnow().isoformat() + 'Z'

    next = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    next = next.isoformat() + 'Z'
    events = {}
    count = 0
    for calendar in calendars:

        try:
            if count == 0:
                events = calendarAPI.events().list(calendarId=calendar["resourceEmail"], timeMin=now,
                                               singleEvents=True, timeMax=next,
                                              orderBy='startTime').execute()["items"]
                count+=1
                continue
            events+= calendarAPI.events().list(calendarId=calendar["resourceEmail"], timeMin=now,
                                               singleEvents=True, timeMax =next,
                                              orderBy='startTime').execute().get('items',[])
        except(HttpError):
            pass

    events = filter(lambda x: x.get("start").get("dateTime") is not None, events)



    newlist = sorted(events, key= lambda x: time.mktime(parse(x.get("start").get("dateTime")).timetuple()))

    context = {
        "events": newlist,
        "building_id": building,
        "room_id": room
    }

    return render(request,"calendar.html",context)

@csrf_exempt
def loadnext(request):
    if request.POST and request.POST.get("buildingId", False) and request.POST.get("date", False):

        building_id = request.POST.get("buildingId")

        room_id = request.POST.get("roomId", False)
        before = request.POST.get("loadBefore", False)

        if room_id is "":
            room_id = False


        if before == "false":
            before = False
        elif before == "true":
            before = True
        # return HttpResponse(before)
        day = request.POST.get("date")

        events = lists.load_more(building_id, day, room_id= room_id, before=before)

        if len(events) <1:

            return HttpResponse(events)

        return JsonResponse(json.dumps({ 'events':events }, ensure_ascii=True), safe=False)

    return HttpResponse(403)


def list(request):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/adm.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    calendarAPI = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = calendarAPI.calendarList().list().execute()
    return HttpResponse( lists.load_more("Ш","2018-08-22T09:00:00+03:00", before=True ))
    return  JsonResponse(json.dumps({ 'events':lists.load_more("Ш","2018-08-23T13:00:00+03:00", before=False) }, ensure_ascii=True), safe=False)


def resources(request):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/adm.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    calendarAPI = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    events_result = calendarAPI.calendarList().list().execute().get("items",[])
    return HttpResponse(events_result)



def buildings(request):
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.resource.calendar']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/adm.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    # credentials.create_delegated("zavaliy@ucu.edu.ua")
    credentials = credentials.with_subject('zavaliy@ucu.edu.ua')
    resourceApi = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

    result = resourceApi.resources().buildings().list(customer="C01ak6gy3").execute()
    # return HttpResponse(result.get("buildings",[]))
    # return JsonResponse(json.dumps(result.get("items",[]), ensure_ascii=False), safe=False)