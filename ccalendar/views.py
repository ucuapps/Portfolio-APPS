from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from google.oauth2 import service_account
from dateutil.parser import parse
import googleapiclient.discovery
import datetime
import json

def index(request):
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/ucu.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    calendarAPI = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = calendarAPI.events().list(calendarId='stasinchuk@ucu.edu.ua', timeMin="2018-03-20T11:30:00+02:00",
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])


    context = {
        "events": events
    }

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
