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
from ccalendar.helpers.lists import calendar_list
from urllib.error import URLError, HTTPError



def index(request):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/adm.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    calendarAPI = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    building = request.GET.get("building","")
    if building is not "":
        calendars = calendar_list(building)
    else:
        calendars = calendar_list("С")
    # calendars = calendar_list("С")
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
    # for event in events:
    #     if event.get("start").get("dateTime") is None:
    #         return HttpResponse(event.get("summary"))

    newlist = sorted(events, key= lambda x: time.mktime(parse(x.get("start").get("dateTime")).timetuple()))

    context = {
        "events": newlist
    }

    # return JsonResponse(json.dumps(events_result.get("items",items,[]), ensure_ascii=False), safe=False)
    # return JsonResponse(json.dumps(context, ensure_ascii=False), safe=False)
    return render(request,"calendar.html",context)

@csrf_exempt
def loadnext(request):
    if request.POST :
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/ucu.json'

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        # registering api
        calendarAPI = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

        now = datetime.datetime.utcnow().isoformat() + 'Z'
        if request.POST.get("loadBefore"):
            events_result = calendarAPI.events().list(calendarId='stasinchuk@ucu.edu.ua',
                                                      timeMax=request.POST.get("date"),
                                                      maxResults=11, singleEvents=True,
                                                      orderBy='startTime').execute()
        else:
            events_result = calendarAPI.events().list(calendarId='stasinchuk@ucu.edu.ua', timeMin=request.POST.get("date"),
                                                  maxResults=11, singleEvents=True,
                                                  orderBy='startTime').execute()
        events = events_result.get('items', [])

        return JsonResponse(json.dumps({ 'events':events }, ensure_ascii=True), safe=False)
    return JsonResponse(json.dumps("go_away", ensure_ascii=True), safe=False)


def list(request):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/adm.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    calendarAPI = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = calendarAPI.calendarList().list().execute()

    return JsonResponse(json.dumps(events_result, ensure_ascii=False), safe=False)


def resources(request):
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.resource.calendar']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/adm.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    # credentials.create_delegated("zavaliy@ucu.edu.ua")
    credentials = credentials.with_subject('zavaliy@ucu.edu.ua')
    resourceApi = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

    result = resourceApi.resources().calendars().list(customer="C01ak6gy3").execute()
    return HttpResponse(calendar_list("Ш"))
    return JsonResponse(json.dumps(result.get("items",[]), ensure_ascii=False), safe=False)


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
    return HttpResponse(result.get("buildings",[]))
    return JsonResponse(json.dumps(result.get("items",[]), ensure_ascii=False), safe=False)